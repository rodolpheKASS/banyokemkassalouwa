document.getElementById('imageUpload').addEventListener('change', function (event) {
    const image = document.getElementById('profileImage');
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        image.src = e.target.result;
    };

    reader.readAsDataURL(file);
});
