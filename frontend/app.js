const textInput = document.getElementById('textInput');
const generateBtn = document.getElementById('generateBtn');
const audioPlayer = document.getElementById('audioPlayer');
const status = document.getElementById('status');

generateBtn.addEventListener('click', async () => {
    const text = textInput.value.trim();
    
    if (!text) {
        status.textContent = 'Please enter some text';
        return;
    }
    
    generateBtn.disabled = true;
    status.textContent = 'Generating speech...';
    
    try {
        const response = await fetch('/api/tts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
        });
        
        if (!response.ok) {
            throw new Error('Failed to generate speech');
        }
        
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        audioPlayer.src = url;
        audioPlayer.play();
        status.textContent = 'Speech generated successfully';
    } catch (error) {
        status.textContent = 'Error: ' + error.message;
    } finally {
        generateBtn.disabled = false;
    }
});
