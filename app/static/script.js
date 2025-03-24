const uploadArea = document.getElementById('uploadArea');
const uploadInput = document.getElementById('uploadInput');
const generateBtn = document.getElementById('generateBtn');
const loading = document.getElementById('loading');
const captionCards = document.getElementById('captionCards');

let uploadedImage = null;

uploadArea.addEventListener('click', () => uploadInput.click());

uploadInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        uploadedImage = e.target.files[0];
        displayImage(uploadedImage);
        generateBtn.disabled = false;
    }
});

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#4361ee';
});

uploadArea.addEventListener('dragleave', () => uploadArea.style.borderColor = '');

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '';

    if (e.dataTransfer.files.length > 0) {
        uploadedImage = e.dataTransfer.files[0];
        displayImage(uploadedImage);
        generateBtn.disabled = false;
    }
});

function displayImage(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
        uploadArea.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image">`;
    };
    reader.readAsDataURL(file);
}

generateBtn.addEventListener('click', () => {
    if (!uploadedImage) return;

    loading.style.display = 'block';
    captionCards.innerHTML = '';

    setTimeout(() => {
        loading.style.display = 'none';
        const captions = [
            "Các cầu thủ bóng đá đang tranh bóng trên sân vận động.",
            "Cầu thủ áo đỏ đang sút bóng về phía khung thành.",
            "Một pha tranh chấp bóng đầy kịch tính giữa hai đội."
        ];

        captions.forEach((caption) => {
            const card = document.createElement('div');
            card.className = 'caption-card';
            card.innerHTML = `<p>${caption}</p>`;
            captionCards.appendChild(card);
        });
    }, 2000);
});
