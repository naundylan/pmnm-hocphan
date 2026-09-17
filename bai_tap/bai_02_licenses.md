| Name               | Version     | License                                            |
|--------------------|-------------|----------------------------------------------------|
| Django             | 6.1.1       | BSD-3-Clause                                       |
| Flask              | 3.1.3       | BSD-3-Clause                                       |
| Jinja2             | 3.1.6       | BSD License                                        |
| MarkupSafe         | 3.0.3       | BSD-3-Clause                                       |
| Pygments           | 2.21.0      | BSD-2-Clause                                       |
| Werkzeug            | 3.1.8       | BSD-3-Clause                                       |
| asgiref            | 3.12.1      | BSD License                                        |
| beautifulsoup4     | 4.15.0      | MIT License                                        |
| blinker            | 1.9.0       | MIT License                                        |
| certifi            | 2026.7.22   | Mozilla Public License 2.0 (MPL 2.0)               |
| charset-normalizer | 3.5.1       | MIT                                                |
| click              | 8.5.0       | BSD-3-Clause                                       |
| contourpy          | 1.4.0       | BSD-3-Clause                                       |
| cycler             | 0.12.1      | BSD License                                        |
| et_xmlfile         | 2.0.0       | MIT License                                        |
| fonttools          | 4.65.0      | MIT                                                |
| idna               | 3.19        | BSD-3-Clause                                       |
| itsdangerous       | 2.2.0       | BSD License                                        |
| kiwisolver         | 1.5.1       | BSD License                                        |
| markdown-it-py     | 4.2.0       | MIT License                                        |
| matplotlib         | 3.11.2      | Python Software Foundation License                 |
| mdurl              | 0.1.2       | MIT License                                        |
| numpy               | 2.5.3       | BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0 |
| openpyxl            | 3.1.5       | MIT License                                        |
| packaging          | 26.3        | Apache-2.0 OR BSD-2-Clause                         |
| pandas              | 3.0.5       | BSD License                                        |
| pillow              | 12.3.0      | MIT-CMU                                            |
| pyparsing           | 3.3.2       | MIT                                                |
| python-dateutil     | 2.9.0.post0 | Apache Software License; BSD License               |
| requests            | 2.34.2      | Apache Software License                            |
| rich                | 15.0.0      | MIT License                                        |
| six                 | 1.17.0      | MIT License                                        |
| soupsieve           | 2.9.2       | MIT                                                |
| sqlparse            | 0.6.0       | BSD License                                        |
| typing_extensions   | 4.16.0      | PSF-2.0                                            |
| tzdata              | 2026.4      | Apache-2.0                                         |
| urllib3             | 2.8.0       | MIT                                                |



### 1. Phân loại và Xác định các nhóm Giấy phép

Dựa trên kết quả truy xuất từ công cụ `pip-licenses`, danh sách các thư viện trong môi trường ảo của dự án được phân loại theo từng nhóm giấy phép như sau:

- **Nhóm Permissive (Tự do / Phổ biến):**
  - *Danh sách thư viện:*
    - **MIT / MIT-compatible:** `beautifulsoup4` (MIT License), `blinker` (MIT License), `charset-normalizer` (MIT), `et_xmlfile` (MIT License), `fonttools` (MIT), `markdown-it-py` (MIT License), `mdurl` (MIT License), `openpyxl` (MIT License), `pyparsing` (MIT), `rich` (MIT License), `six` (MIT License), `soupsieve` (MIT), `urllib3` (MIT).
    - **BSD:** `Django` (BSD-3-Clause), `Flask` (BSD-3-Clause), `Jinja2` (BSD License), `MarkupSafe` (BSD-3-Clause), `Pygments` (BSD-2-Clause), `Werkzeug` (BSD-3-Clause), `asgiref` (BSD License), `click` (BSD-3-Clause), `contourpy` (BSD-3-Clause), `cycler` (BSD License), `idna` (BSD-3-Clause), `itsdangerous` (BSD License), `kiwisolver` (BSD License), `pandas` (BSD License), `sqlparse` (BSD License).
    - **Apache / PSF / Python Software Foundation:** `requests` (Apache Software License), `packaging` (Apache-2.0 OR BSD-2-Clause), `python-dateutil` (Apache Software License; BSD License), `typing_extensions` (PSF-2.0), `tzdata` (Apache-2.0), `matplotlib` (Python Software Foundation License).
    - **Các giấy phép đa thành phần:** `numpy` (BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0), `pillow` (MIT-CMU).
  - *Đặc điểm:* Đây là các giấy phép cho phép sử dụng, sửa đổi và phân phối phần mềm, kể cả trong sản phẩm thương mại đóng nguồn, với điều kiện tuân thủ các nghĩa vụ đi kèm. Các nghĩa vụ thường bao gồm giữ lại thông báo bản quyền, văn bản giấy phép và các điều khoản liên quan. Nhóm này không áp đặt nghĩa vụ mở mã nguồn toàn bộ ứng dụng chỉ vì sử dụng thư viện.

- **Nhóm Weak Copyleft (Copyleft yếu):**
  - *Danh sách thư viện:* `certifi` (Mozilla Public License 2.0 - MPL 2.0).
  - *Đặc điểm:* MPL-2.0 là giấy phép copyleft yếu ở cấp độ tệp. Khi sửa đổi các tệp mã nguồn được cấp phép theo MPL và phân phối chúng, các tệp đã sửa đổi đó thường phải tiếp tục được cung cấp theo MPL-2.0. Tuy nhiên, việc kết hợp các tệp MPL với mã nguồn riêng trong một chương trình lớn hơn không mặc nhiên buộc toàn bộ mã nguồn riêng phải công khai theo MPL.

- **Nhóm Strong Copyleft (Copyleft mạnh - GPLv2, GPLv3, AGPLv3):**
  - **Không xuất hiện gói nào** có giấy phép GPL, AGPL hoặc giấy phép copyleft mạnh tương đương trong danh sách phân tích.
  - *Lưu ý:* Kết luận này áp dụng cho các gói và giấy phép được hiển thị trong kết quả `pip-licenses`. Để đánh giá đầy đủ một sản phẩm, cần kiểm tra cả các dependency gián tiếp và các thành phần khác được phân phối cùng phần mềm.

---

### 2. Phân tích Nghĩa vụ Pháp lý đối với Dự án Thương mại Đóng nguồn

Nếu dự án được phát triển và thương mại hóa dưới dạng một **Phần mềm thương mại đóng nguồn (Proprietary Closed-Source Software)**, các nghĩa vụ pháp lý phát sinh được xác định như sau:

#### A. Đối với các thư viện nhóm Permissive (MIT, BSD, Apache, PSF)

- **Nghĩa vụ giữ thông báo bản quyền và giấy phép:** Dự án phải tuân thủ các điều kiện của từng giấy phép. Với MIT, BSD và Apache-2.0, nghĩa vụ phổ biến là giữ lại thông báo bản quyền, văn bản giấy phép và các thông báo liên quan khi phân phối phần mềm hoặc bản sao của thư viện.
- **Đối với Apache-2.0:** Ngoài các nghĩa vụ về bản quyền và giấy phép, cần chú ý các điều khoản liên quan đến thông báo thay đổi và bằng sáng chế theo phạm vi áp dụng của giấy phép.
- **Đối với các giấy phép đa thành phần:** `numpy` có nhiều thành phần giấy phép được công cụ hiển thị dưới dạng `BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0`. Dự án cần bảo đảm tuân thủ các điều kiện áp dụng của từng thành phần, thay vì chỉ ghi nhận một giấy phép duy nhất.
- **Quyền giữ kín mã nguồn:** Các giấy phép permissive nêu trên nhìn chung cho phép dự án giữ kín mã nguồn nghiệp vụ tự phát triển. Việc sử dụng thư viện không tự động làm phát sinh nghĩa vụ công khai toàn bộ mã nguồn của ứng dụng.
- **Tài liệu tuân thủ:** Nên lưu trữ bản sao giấy phép và thông báo bản quyền của các thư viện trong thư mục như `LICENSES`, `THIRD-PARTY-NOTICES` hoặc mục *Legal/About* của sản phẩm.

#### B. Đối với thư viện `certifi` - MPL-2.0 (Weak Copyleft)

- **Khả năng đóng nguồn dự án:** MPL-2.0 là copyleft yếu ở cấp độ tệp. Việc sử dụng `certifi` trong một ứng dụng thương mại không tự động buộc toàn bộ mã nguồn ứng dụng phải công khai. Tuy nhiên, các nghĩa vụ của MPL-2.0 vẫn phải được tuân thủ khi phân phối phần mềm.
- **Nghĩa vụ phát sinh cụ thể:**
  1. **Giữ thông báo và văn bản giấy phép:** Dự án cần giữ lại các thông báo bản quyền, thông báo giấy phép và các thông tin cần thiết của `certifi` khi phân phối sản phẩm.
  2. **Đối với tệp được sửa đổi:** Nếu nhóm phát triển sửa đổi các tệp thuộc phạm vi MPL-2.0 và phân phối các tệp đó, các tệp sửa đổi phải được cung cấp theo MPL-2.0 theo các điều kiện của giấy phép.
  3. **Cung cấp mã nguồn tương ứng khi cần:** Khi phân phối các tệp MPL đã sửa đổi, cần cung cấp mã nguồn tương ứng theo phương thức được MPL-2.0 cho phép và yêu cầu.
  4. **Không mở rộng nghĩa vụ sang toàn bộ ứng dụng:** Mã nguồn nghiệp vụ riêng của dự án có thể tiếp tục đóng nguồn nếu không thuộc phạm vi các tệp phải cung cấp theo MPL-2.0.
  5. **Kiểm tra thành phần thực tế:** Cần xác định chính xác các tệp và thành phần nào của `certifi` được phân phối cùng sản phẩm để áp dụng đúng nghĩa vụ giấy phép.

#### C. Đối với nhóm Strong Copyleft (GPL / AGPL)

- **Kết quả kiểm tra:** Không phát hiện gói nào có giấy phép GPL hoặc AGPL trong danh sách `pip-licenses` đã truy xuất.
- **Nghĩa vụ nếu sau này sử dụng GPL:** Nếu dự án bổ sung một thư viện GPL và việc kết hợp, liên kết hoặc phân phối thuộc phạm vi áp dụng của GPL, dự án có thể phải phân phối phần mềm theo GPL và cung cấp mã nguồn tương ứng theo các điều kiện của giấy phép.
- **Nghĩa vụ nếu sử dụng AGPL:** AGPL có các nghĩa vụ copyleft tương tự GPL và có thêm quy định liên quan đến việc cung cấp phần mềm qua mạng. Điều này cần được xem xét đặc biệt đối với ứng dụng web hoặc dịch vụ SaaS.
- **Kết luận đối với danh sách hiện tại:** Do không phát hiện GPL hoặc AGPL, danh sách hiện tại không cho thấy nghĩa vụ copyleft mạnh buộc toàn bộ ứng dụng phải mở nguồn. Tuy nhiên, kết luận này không thay thế việc kiểm tra toàn bộ dependency và các thành phần được phân phối.

---

### 3. Kết luận

Kết quả `pip-licenses` cho thấy môi trường ảo của dự án chủ yếu sử dụng các thư viện có giấy phép permissive như MIT, BSD, Apache và PSF. Các giấy phép này nhìn chung phù hợp với việc phát triển phần mềm thương mại đóng nguồn, miễn là dự án tuân thủ các điều kiện về bản quyền, giấy phép và các thông báo liên quan.

Trong danh sách có `certifi` sử dụng MPL-2.0, thuộc nhóm copyleft yếu. MPL-2.0 không tự động buộc toàn bộ ứng dụng phải công khai mã nguồn, nhưng có thể phát sinh nghĩa vụ cung cấp mã nguồn đối với các tệp MPL đã sửa đổi và phân phối.

Không phát hiện gói nào thuộc nhóm strong copyleft như GPL hoặc AGPL trong kết quả kiểm tra. Vì vậy, dựa trên danh sách hiện tại, chưa ghi nhận nghĩa vụ mở mã nguồn toàn bộ ứng dụng do sử dụng thư viện strong copyleft.

Để bảo đảm tuân thủ khi thương mại hóa, nhóm phát triển nên:

- Kiểm tra giấy phép của cả dependency trực tiếp và gián tiếp.
- Lưu trữ bản sao giấy phép và thông báo bản quyền của các thư viện.
- Ghi nhận các thay đổi đối với thư viện bên thứ ba.
- Kiểm tra riêng các thư viện có giấy phép copyleft như MPL, LGPL, GPL hoặc AGPL.
- Đánh giá cách tích hợp và phân phối thực tế trước khi phát hành sản phẩm.
