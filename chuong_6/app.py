import os
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key"
# Flask-SQLAlchemy tự động lưu file qlsv.db vào thư mục instance/ (instance/qlsv.db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///qlsv.db"

# Header trả về văn bản thuần để trình duyệt không hiểu nhầm <Student ...> là thẻ HTML
TEXT = {"Content-Type": "text/plain; charset=utf-8"}


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# =======================================================
# Bước 3. Khai báo model Student
# =======================================================
class Student(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    mssv: Mapped[str] = mapped_column(String(10), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    gpa: Mapped[float] = mapped_column(default=0.0)

    def __repr__(self):
        return f"<Student {self.mssv} {self.name}>"


# Tự động tạo bảng trong CSDL (instance/qlsv.db) nếu chưa có
with app.app_context():
    os.makedirs(app.instance_path, exist_ok=True)
    db.create_all()


# =======================================================
# Route mới: Render template chứa bảng trống (sẵn sàng hiển thị Student sau này)
# =======================================================
@app.route("/")
@app.get("/danh-sach")
def student_list():
    # Mặc định truyền danh sách trống để hiển thị bảng trống theo yêu cầu.
    # Khi muốn hiển thị dữ liệu từ CSDL, bạn chỉ cần thay bằng:
    # students = Student.query.order_by(Student.id).all()
    students = []
    
    # Nếu muốn xem dữ liệu thật trong CSDL trên bảng này, có thể mở ?hien_thi=1
    if request.args.get("hien_thi") == "1":
        students = Student.query.order_by(Student.id).all()

    return render_template("danh_sach.html", students=students)


# =======================================================
# Bước 5. Thêm dữ liệu bằng view function
# =======================================================
@app.get("/them-mau")
def add_sample():
    total = db.session.scalar(db.select(func.count(Student.id)))
    if total > 0:
        return f"Đã có {total} sinh viên, không thêm nữa."

    an = Student(mssv="23T1020001", name="Nguyễn Văn An", gpa=8.5)
    before = an.id  # chưa ghi xuống CSDL (None)
    db.session.add(an)  # đưa vào "giỏ" chờ ghi

    db.session.add_all(
        [
            Student(mssv="23T1020002", name="Trần Thị Bình", gpa=6.8),
            Student(mssv="23T1020003", name="Lê Hoàng Cường", gpa=9.1),
            Student(mssv="23T1020004", name="Phạm Minh Dũng", gpa=4.5),
            Student(mssv="23T1020005", name="Hoàng Thu Hà", gpa=7.4),
        ]
    )
    db.session.commit()  # ghi thật sự xuống file qlsv.db

    return (
        f"Đã thêm 5 sinh viên. id của An: "
        f"trước commit = {before}, "
        f"sau commit = {an.id}"
    )


# =======================================================
# Bước 6. Đọc dữ liệu bằng view function
# =======================================================
@app.get("/thu-truy-van")
def try_queries():
    if db.session.scalar(db.select(func.count(Student.id))) == 0:
        return "Chưa có dữ liệu, hãy mở /them-mau trước.", TEXT

    lines = []
    lines.append(f"1. get(3): {db.session.get(Student, 3)}")
    lines.append(f"2. get(99): {db.session.get(Student, 99)}")

    everyone = db.session.execute(db.select(Student)).scalars().all()
    lines.append(f"3. Tất cả: {len(everyone)} sinh viên")

    stmt = (
        db.select(Student)
        .where(Student.gpa >= 8)
        .order_by(Student.gpa.desc())
    )
    good = db.session.execute(stmt).scalars().all()
    lines.append(f"4. Điểm >= 8: {good}")

    binh = db.session.scalar(
        db.select(Student).filter_by(mssv="23T1020002")
    )
    lines.append(f"5. MSSV 23T1020002: {binh}")

    count = db.session.scalar(db.select(func.count(Student.id)))
    avg = db.session.scalar(db.select(func.avg(Student.gpa)))
    lines.append(f"6. Số SV: {count}, điểm TB: {avg:.2f}")

    return "\n".join(lines), TEXT


if __name__ == "__main__":
    app.run(debug=True, port=5000)
