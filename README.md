# Kho lưu trữ môn học: PMNM-HOCPHAN

## 1. Thông tin cá nhân
- **Họ và tên:** Ngô Lê Nam Quyền
- **Mã sinh viên:** 23T1020436
- **Lớp:** PMMNM N2

---

## 2. Lý do tôi muốn học về Phần mềm Mã nguồn Mở

Tôi muốn học học phần Phần mềm mã nguồn mở vì đây là cánh cửa mở ra thế giới công nghệ hiện đại, nơi tri thức được chia sẻ tự do và minh bạch. Môn[...]

---

## 3. Danh sách 5 phần mềm mã nguồn mở sử dụng hằng ngày

| STT | Tên phần mềm / Môi trường | Công dụng chính | Giấy phép mã nguồn mở (License) |
| :---: | :--- | :--- | :--- |
| **1** | **Git** | Hệ thống quản lý phiên bản mã nguồn phân tán. | **GNU General Public License v2.0 (GPLv2)** |
| **2** | **VS Code (Code - OSS)** | Trình soạn thảo mã nguồn và phát triển ứng dụng. | **MIT License** |
| **3** | **PostgreSQL** | Hệ quản trị cơ sở dữ liệu quan hệ mã nguồn mở. | **PostgreSQL License** |
| **4** | **OpenJDK (Java JDK)** | Bộ công cụ phát triển ứng dụng ngôn ngữ Java. | **GNU GPLv2 with Classpath Exception** |
| **5** | **Node.js (JavaScript)** | Môi trường thực thi JavaScript mã nguồn mở. | **MIT License** |

---

## 4. Phân tích trường hợp: Rẽ nhánh Elasticsearch và OpenSearch

### 4.1 Giới thiệu về dự án

Elasticsearch là một công cụ tìm kiếm và phân tích dữ liệu mã nguồn mở được phát triển bởi công ty Elastic. Nó được sử dụng rộng rãi trong việc xây dựng các hệ thống tìm kiếm, phân tích log, và giám sát hiệu suất. Tuy nhiên, năm 2021, một trong những sự kiện quan trọng nhất trong lịch sử phần mềm mã nguồn mở đã xảy ra: Elastic đã thay đổi giấy phép của Elasticsearch từ Elastic License và SSPL (Server Side Public License) thay vì tiếp tục sử dụng AGPL hoặc GPL. Quyết định này đã gây ra tranh cãi lớn và dẫn đến sự rẽ nhánh lớn nhất trong cộng đồng.

### 4.2 Nguyên nhân dẫn đến rẽ nhánh

**Tranh chấp về giấy phép và quyền lợi:**
Elastic đã thay đổi chính sách giấy phép nhằm bảo vệ lợi nhuận của họ. Phiên bản Elasticsearch 7.11 trở đi không còn là mã nguồn mở hoàn toàn theo định nghĩa của Open Source Initiative (OSI). Thay vào đó, chỉ các phiên bản cũ hơn (trước 7.11) vẫn được coi là mã nguồn mở thực sự. Điều này đã vi phạm một trong những nguyên tắc cơ bản của cộng đồng mã nguồn mở: tự do sử dụng, sửa đổi, và phân phối mã nguồn.

**Phản ứng mạnh mẽ từ cộng đồng:**
Cộng đồng mã nguồn mở, đặc biệt là các nhà phát triển của AWS, đã nhanh chóng phản ứng. Amazon Web Services (AWS), một công ty lớn và có sức ảnh hưởng, đã ra mắt dự án OpenSearch vào tháng 9 năm 2021 bằng cách fork từ Elasticsearch 7.10 (phiên bản cuối cùng được phát hành theo Elastic License).

### 4.3 Sự phát triển của OpenSearch

**OpenSearch được xây dựng dựa trên:**
- Fork từ Elasticsearch 7.10, giữ lại tính chất mã nguồn mở hoàn toàn
- Được phát hành dưới giấy phép Elastic License và Server Side Public License (SSPL), nhưng AWS đã phát triển nó theo hướng mã nguồn mở thực sự
- Tập trung vào việc phát triển các tính năng mới, cải thiện hiệu suất, và duy trì sự tương thích với Elasticsearch

**Những lợi ích khi chuyển sang OpenSearch:**
- Hoàn toàn mã nguồn mở và miễn phí
- Được hỗ trợ bởi AWS, một công ty có tài nguyên lớn
- Không bị ràng buộc bởi chính sách thay đổi giấy phép đột ngột
- Cộng đồng phát triển sôi nổi và tích cực

### 4.4 Kết quả và bài học

**Những hậu quả từ rẽ nhánh:**
1. **Chia cắt cộng đồng:** Cộng đồng Elasticsearch đã bị chia cắt. Một số công ty tiếp tục sử dụng Elasticsearch với giấy phép thương mại, trong khi những công ty khác chuyển sang OpenSearch.

2. **Sự suy giảm uy tín:** Quyết định của Elastic đã làm giảm uy tín và lòng tin của cộng đồng mã nguồn mở đối với công ty này, chứng tỏ rằng lợi nhuận có thể được ưu tiên hơn tinh thần mã nguồn mở.

3. **OpenSearch phát triển mạnh mẽ:** OpenSearch đã trở thành một lựa chọn thực sự cạnh tranh, với hàng triệu tải xuống và sự hỗ trợ từ cộng đồng lớn.

**Bài học quan trọng:**
- Tính minh bạch và tính nhất quán trong giấy phép là cực kỳ quan trọng trong dự án mã nguồn mở
- Cộng đồng luôn có cách để "cứu vãn" một dự án khi công ty phát triển chính thức bỏ rơi các nguyên tắc cơ bản
- Mâu thuẫn về lợi nhuận và mã nguồn mở thực sự có thể dẫn đến những rẽ nhánh lớn và chia cắt cộng đồng
- Các công ty nên cân nhắc kỹ lưỡng các quyết định liên quan đến giấy phép, vì nó có thể ảnh hưởng trực tiếp đến sự phát triển và mức độ tín nhiệm của dự án
