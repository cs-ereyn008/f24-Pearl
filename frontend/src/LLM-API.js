const API_URL = "https://api-inference.huggingface.co/models/saul-ai/SaulLM-7B";
const API_KEY = "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";
//normally I wouldn't make this key accessible on the frontend, 
//but if we're not actually deploying it to the internet it should be fine 

async function simplifyText(text) {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            Authorization: `Bearer ${API_KEY}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ inputs: text }),
    });

    const result = await response.json();
    if (result && result[0] && result[0].generated_text) {
        return result[0].generated_text;
    } else {
        throw new Error("Error simplifying text");
    }
}

document.getElementById("simplify-button").addEventListener("click", async () => {
    const textInput = document.getElementById("legal-text").value;
    try {
        const simplifiedText = await simplifyText(textInput);
        document.getElementById("result").innerText = simplifiedText;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error processing text";
    }
});

//link API in HTML using <script src="LLM-API.js"></script>