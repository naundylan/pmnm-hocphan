# Bài 01: Tragedy of the Commons trong Phần Mềm Mã Nguồn Mở

## Giới thiệu

Tragedy of the Commons (Thảm họa của các bộ lạc chung) là một khái niệm kinh tế mô tả tình trạng khi các cá nhân hoặc tổ chức, theo lợi ích cá nhân, khai thác quá mức các tài nguyên công cộng mà không ai sở hữu, dẫn đến suy thoái hoặc hủy hoại tài nguyên đó. Trong lĩnh vực phần mềm mã nguồn mở, hiện tượng này xuất hiện rõ rệt: hàng trăm, thậm chí hàng ngàn tổ chức và cá nhân sử dụng các thư viện hạ tầng cốt lõi miễn phí, nhưng rất ít tổ chức chủ động tài trợ hoặc hỗ trợ bảo trì các dự án này.

## OpenSSL: Một Trường Hợp Điển Hình

OpenSSL là một thư viện mã nguồn mở cung cấp các công cụ và thư viện cho mã hóa SSL/TLS. Nó được sử dụng rộng rãi trong hàng triệu máy chủ web, ứng dụng, và hệ thống trên toàn thế giới. Trước năm 2014, OpenSSL chỉ có một đội ngũ bảo trì cực kỳ nhỏ — chủ yếu là một hoặc hai lập trình viên tình nguyện.

### Lỗ hổng Heartbleed (2014)

Năm 2014, lỗ hổng bảo mật nghiêm trọng gọi là "Heartbleed" được phát hiện trong OpenSSL. Lỗ hổng này cho phép các attacker trích xuất thông tin nhạy cảm từ bộ nhớ, bao gồm khóa mã hóa và dữ liệu người dùng. Điều đáng lo ngại là lỗ hổng này tồn tại hơn hai năm mà không ai phát hiện ra.

Heartbleed tiết lộ một sự thật khắc nghiệt: một thư viện mà hầu như toàn bộ internet phụ thuộc vào lại được bảo trì bởi những người tình nguyện không có nguồn tài chính đầy đủ. Các tổ chức lớn như Google, Facebook, Amazon sử dụng OpenSSL hàng ngày nhưng không có ai tài trợ cho việc bảo trì, kiểm tra mã, hoặc cải thiện quy trình phát triển.

### Nguyên Nhân của Thảm Họa

Tragedy of the Commons trong trường hợp OpenSSL phát sinh từ:

1. **Lợi ích cá nhân của các tổ chức**: Mỗi công ty sử dụng OpenSSL để xây dựng sản phẩm của mình mà không cần phải trả tiền, tiết kiệm chi phí phát triển.

2. **Thiếu động lực tài trợ**: Không có tổ chức nào muốn tài trợ một dự án công cộng khi các đối thủ cạnh tranh cũng được hưởng lợi mà không trả tiền.

3. **Sự không rõ ràng về trách nhiệm**: Không ai cảm thấy mình có trách nhiệm bảo trì hoặc cải thiện OpenSSL vì nó không thuộc sở hữu của bất kỳ ai.

4. **Tình trạng "free-rider"**: Tất cả các tổ chức đều hưởng lợi từ OpenSSL nhưng ít ai đóng góp, tạo thành hành vi "free-rider" lan rộng.

## Tác Động của Heartbleed

Heartbleed được coi là một trong những lỗ hổng bảo mật nghiêm trọng nhất trong lịch sử internet. Nó ảnh hưởng đến:

- Hàng triệu máy chủ web
- Các dịch vụ email, mạng xã hội, và ngân hàng trực tuyến
- Độ tin tưởng của công chúng vào an niệm mạng

Sự kiện này cho thấy rõ ràng rằng khi tài nguyên công cộng (OpenSSL) không được hỗ trợ cung cấp, nó trở thành điểm yếu nguy hiểm cho toàn bộ hệ thống.

## Cơ Chế Khắc Phục

Để giải quyết vấn đề này, có thể áp dụng các cơ chế sau:

### 1. Mô Hình Tài Trợ Hợp Tác

Các tổ chức sử dụng OpenSSL có thể hình thành một liên minh tài trợ chung. Mỗi tổ chức đóng góp một phần kinh phí theo mức độ sử dụng hoặc lợi nhuận của họ. Mô hình này tương tự như "Apache Software Foundation" nơi các công ty tài trợ cho các dự án mã nguồn mở.

### 2. Chính Sách Bắt Buộc

Các chính phủ hoặc các tổ chức quốc tế có thể thiết lập quy định yêu cầu các công ty sử dụng phần mềm mã nguồn mở phải đóng góp một phần doanh thu hoặc nhân lực để bảo trì các dự án đó.

### 3. Kiểm Toán và Sertifikation

Tạo một quy trình kiểm toán định kỳ và sertifikation cho các thư viện hạ tầng quan trọng. Các tổ chức sử dụng những thư viện này phải tài trợ cho quá trình kiểm toán an niệm.

### 4. Mô Hình Giấy Phép Hợp Lý

Áp dụng các giấy phép yêu cầu các công ty thương mại sử dụng phần mềm mã nguồn mở phải đóng góp hoặc cấp phép (ví dụ: mô hình "Commons Clause").

### 5. Hệ Thống Tích Điểm Lợi Nhuận

Tạo một hệ thống trong đó các công ty có thể kiếm điểm hoặc nhận được đặc quyền nếu họ đóng góp vào các dự án mã nguồn mở quan trọng.

## Kết Luận

Tragedy of the Commons trong OpenSSL cho thấy một vấn đề sâu sắc trong mô hình phát triển phần mềm mã nguồn mở hiện tại. Mặc dù mã nguồn mở mang lại nhiều lợi ích cho xã hội, nhưng nếu không có cơ chế tài trợ rõ ràng, các dự án cốt lõi sẽ bị bỏ bê và trở thành rủi ro bảo mật cho toàn bộ hệ thống.

Để khắc phục, cần phải thay đổi cách chúng ta nhìn nhận giá trị của phần mềm mã nguồn mở. Các tổ chức sử dụng những thư viện này phải hiểu rằng hỗ trợ và tài trợ bảo trì không phải là một khoản chi phí vô ích, mà là một khoản đầu tư quan trọng cho bảo mật và ổn định của toàn bộ hệ thống thông tin.

Sau sự kiện Heartbleed, tình huống đã cải thiện phần nào với các sáng kiến như "Core Infrastructure Initiative" (ngày nay là "Open Source Security Foundation") do Linux Foundation lãnh đạo, nhưng vẫn còn rất nhiều thư viện mã nguồn mở khác chưa nhận được sự hỗ trợ đủ.
