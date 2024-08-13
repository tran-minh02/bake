// // Gửi yêu cầu đến API để lấy dữ liệu người dùng
// fetch('/api/users/')
//     .then(response => {
//         if (!response.ok) {
//             throw new Error('Network response was not ok ' + response.statusText);
//         }
//         return response.json(); // Chuyển đổi phản hồi thành JSON
//     })
//     .then(data => {
//         console.log(data); // In dữ liệu người dùng ra console để kiểm tra
//         // Bạn có thể gọi một hàm để hiển thị dữ liệu này trên trang web
//         displayUsers(data);
//     })
//     .catch(error => {
//         console.error('There has been a problem with your fetch operation:', error);
//     });
