/**
 * Keshunte Pravajanam (കേശുവിന്റെ പ്രവചനം)
 * Frontend Interactive Logic & Sound Engine
 * Designed for College Useless Project Competition
 */

document.addEventListener("DOMContentLoaded", function () {
    // DOM Elements
    const nameInput = document.getElementById("userName");
    const nakshatramSelect = document.getElementById("nakshatram");
    const favSnackSelect = document.getElementById("favSnack");
    const currentMoodSelect = document.getElementById("currentMood");
    const predictBtn = document.getElementById("predictBtn");
    const loadingBox = document.getElementById("loadingBox");
    const loadingText = document.getElementById("loadingText");
    const progressBar = document.getElementById("progressBar");
    const resultBox = document.getElementById("resultBox");
    const soundToggleBtn = document.getElementById("soundToggleBtn");
    const soundStatus = document.getElementById("soundStatus");
    const soundIcon = document.getElementById("soundIcon");
    const tryAgainBtn = document.getElementById("tryAgainBtn");
    const shareWhatsappBtn = document.getElementById("shareWhatsappBtn");
    const speakBtn = document.getElementById("speakBtn");
    const printBtn = document.getElementById("printBtn");
    const lemonBanner = document.querySelector(".lemon-chilli-banner");
    const confettiCanvas = document.getElementById("confettiCanvas");

    // Sound System Configuration
    let isSoundEnabled = localStorage.getItem("keshuSound") !== "false";
    updateSoundButtonUI();

    // Audio Context (Synthesizer for comical zero-dependency sound effects)
    let audioCtx = null;

    function getAudioContext() {
        if (!audioCtx) {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            if (AudioContextClass) {
                audioCtx = new AudioContextClass();
            }
        }
        if (audioCtx && audioCtx.state === "suspended") {
            audioCtx.resume();
        }
        return audioCtx;
    }

    // Sound 1: Comical Spring Boing (on button press)
    function playBoingSound() {
        if (!isSoundEnabled) return;
        try {
            const ctx = getAudioContext();
            if (!ctx) return;
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            const now = ctx.currentTime;

            osc.type = "sine";
            osc.frequency.setValueAtTime(150, now);
            osc.frequency.exponentialRampToValueAtTime(600, now + 0.15);
            osc.frequency.exponentialRampToValueAtTime(250, now + 0.3);

            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);

            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(now);
            osc.stop(now + 0.36);
        } catch (e) {
            console.warn("Audio play error:", e);
        }
    }

    // Sound 2: Cosmic Chime (during astrology calculation)
    function playCosmicChime(freq = 440) {
        if (!isSoundEnabled) return;
        try {
            const ctx = getAudioContext();
            if (!ctx) return;
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            const now = ctx.currentTime;

            osc.type = "triangle";
            osc.frequency.setValueAtTime(freq, now);
            gain.gain.setValueAtTime(0.15, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);

            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(now);
            osc.stop(now + 0.41);
        } catch (e) {
            console.warn("Audio error:", e);
        }
    }

    // Sound 3: Victory / Fanfare Chords on Reveal
    function playVictoryChimes() {
        if (!isSoundEnabled) return;
        try {
            const notes = [330, 440, 554, 659, 880];
            notes.forEach((note, index) => {
                setTimeout(() => {
                    playCosmicChime(note);
                }, index * 90);
            });
        } catch (e) {
            console.warn("Audio error:", e);
        }
    }

    // Toggle Sound
    soundToggleBtn.addEventListener("click", () => {
        isSoundEnabled = !isSoundEnabled;
        localStorage.setItem("keshuSound", isSoundEnabled);
        updateSoundButtonUI();
        if (isSoundEnabled) {
            playCosmicChime(523.25);
        }
    });

    function updateSoundButtonUI() {
        if (isSoundEnabled) {
            soundStatus.textContent = "ON";
            soundIcon.textContent = "🔊";
            soundToggleBtn.style.borderColor = "var(--gold-primary)";
        } else {
            soundStatus.textContent = "OFF";
            soundIcon.textContent = "🔇";
            soundToggleBtn.style.borderColor = "rgba(255,255,255,0.2)";
        }
    }

    // Interactive Lemon Banner click
    if (lemonBanner) {
        lemonBanner.addEventListener("click", () => {
            playCosmicChime(784);
            alert("🍋 ദൃഷ്ടിദോഷം 100% ഒഴിഞ്ഞുപോയി! ഇനി കേശുവിന്റെ പ്രവചനം നോക്കാം!");
        });
    }

    // Loading stages in Malayalam
    const LOADING_STEPS = [
        { progress: 15, text: "കവടി നിരത്തുന്നു... 🐚" },
        { progress: 40, text: "ശനി, രാഹു, കേതു എന്നിവരുമായി കോൺഫറൻസ് കാൾ... 🪐" },
        { progress: 65, text: "ജ്യോതിഷ ഡാറ്റാബേസ് ഹാക്ക് ചെയ്യുന്നു... 📡" },
        { progress: 85, text: "കേശു ചായ കുടിച്ചു തിരിച്ചെത്തുന്നു... ☕" },
        { progress: 100, text: "മഹാജാതകം റെഡി! 📜✨" }
    ];

    // Main button: "പ്രവചനം പറയൂ" Click Handler
    predictBtn.addEventListener("click", generatePrediction);

    // Also support Enter key inside name input
    nameInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            e.preventDefault();
            generatePrediction();
        }
    });

    let currentPredictionData = null;

    async function generatePrediction() {
        const userName = nameInput.value.trim();

        // If name is empty, highlight field with funny prompt
        if (!userName) {
            nameInput.focus();
            nameInput.style.borderColor = "#ff007f";
            nameInput.style.boxShadow = "0 0 20px rgba(255, 0, 127, 0.8)";
            
            playBoingSound();

            setTimeout(() => {
                alert("ദയവായി നിങ്ങളുടെ പേര് നൽകൂ... പേര് കാണാതെ കേശുവിന് കവടി നിരത്താൻ പറ്റില്ല! 😂");
                nameInput.style.borderColor = "";
                nameInput.style.boxShadow = "";
            }, 100);
            return;
        }

        // Play action sound
        playBoingSound();

        // UI Transition to Loading State
        predictBtn.disabled = true;
        predictBtn.style.opacity = "0.7";
        resultBox.classList.add("hidden");
        loadingBox.classList.remove("hidden");
        progressBar.style.width = "0%";

        // Scroll to loading card
        loadingBox.scrollIntoView({ behavior: "smooth", block: "center" });

        // Execute dynamic Malayalam loading steps
        let stepIdx = 0;
        const stepInterval = setInterval(() => {
            if (stepIdx < LOADING_STEPS.length) {
                loadingText.textContent = LOADING_STEPS[stepIdx].text;
                progressBar.style.width = LOADING_STEPS[stepIdx].progress + "%";
                playCosmicChime(300 + stepIdx * 90);
                stepIdx++;
            } else {
                clearInterval(stepInterval);
            }
        }, 320);

        try {
            // Fetch prediction from Flask backend API
            const response = await fetch("/api/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    name: userName,
                    nakshatram: nakshatramSelect ? nakshatramSelect.value : "",
                    favSnack: favSnackSelect ? favSnackSelect.value : "",
                    currentMood: currentMoodSelect ? currentMoodSelect.value : ""
                })
            });

            const data = await response.json();
            currentPredictionData = data;

            // Ensure loading animation runs for at least 1.6s for comedic timing
            setTimeout(() => {
                clearInterval(stepInterval);
                displayPrediction(data);
            }, 1600);

        } catch (error) {
            console.error("Prediction fetch failed, using offline fallback:", error);
            setTimeout(() => {
                clearInterval(stepInterval);
                const fallbackData = getOfflinePrediction(userName);
                currentPredictionData = fallbackData;
                displayPrediction(fallbackData);
            }, 1600);
        }
    }

    function displayPrediction(data) {
        // Populate Result Fields
        document.getElementById("resultUserTitle").textContent = data.title || `ശ്രീ/ശ്രീമതി ${data.name} അവരുടെ മഹാജാതകം 📜`;
        document.getElementById("resultTagline").textContent = data.tagline || "മഹാരാജയോഗം!";
        document.getElementById("resultPredictionText").textContent = data.prediction;
        document.getElementById("resultAccuracy").textContent = data.accuracy || "0.01%";
        
        document.getElementById("resultMovieCharacter").textContent = data.movie_character || "ദശമൂലം ദാമു";
        document.getElementById("resultMovieDialogue").textContent = data.movie_dialogue || "കോൺഫിഡൻസ് അൺലിമിറ്റഡ്!";

        document.getElementById("resultDoshamName").textContent = data.dosham || "റീൽസ് അഡിക്ഷൻ ദോഷം";
        document.getElementById("resultDoshamDesc").textContent = data.dosham_desc || "കണ്ണിൽ എപ്പോഴും ഫോൺ സ്ക്രീൻ മാത്രം.";
        document.getElementById("resultRemedy").textContent = data.remedy;

        document.getElementById("resultLuckyNumber").textContent = data.lucky_number || "420";
        document.getElementById("resultLuckyColor").textContent = data.lucky_color || "കട്ടൻ ചായ കളർ";
        document.getElementById("resultLuckyFood").textContent = data.lucky_food || "പൊറോട്ട & ബീഫ്";
        document.getElementById("resultCareer").textContent = data.best_career || "കവലയിലെ രാഷ്ട്രീയ നിരീക്ഷകൻ";

        document.getElementById("resultQuote").textContent = data.keshu_quote || "“ജാതകം നോക്കി പേടിക്കേണ്ട, ജീവിച്ചു പേടിച്ചാൽ മതി!” — കേശു സ്വാമി";

        // Hide Loading, Reveal Result
        loadingBox.classList.add("hidden");
        resultBox.classList.remove("hidden");
        predictBtn.disabled = false;
        predictBtn.style.opacity = "1";

        // Play victory sounds & confetti
        playVictoryChimes();
        launchConfetti();

        // Smooth scroll to result
        resultBox.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    // "വീണ്ടും നോക്കൂ" (Try Again) Button
    if (tryAgainBtn) {
        tryAgainBtn.addEventListener("click", () => {
            playBoingSound();
            generatePrediction();
        });
    }

    // "WhatsApp-ൽ ഷെയർ ചെയ്യൂ" Button
    if (shareWhatsappBtn) {
        shareWhatsappBtn.addEventListener("click", () => {
            if (!currentPredictionData) return;
            const text = `🔮 *കേശുവിന്റെ പ്രവചനം (Keshunte Pravajanam)* 🔮\n\n` +
                         `📜 *പേര്:* ${currentPredictionData.name}\n` +
                         `✨ *പ്രവചനം:* ${currentPredictionData.prediction}\n` +
                         `⚠️ *ദോഷം:* ${currentPredictionData.dosham}\n` +
                         `🌿 *പരിഹാരം:* ${currentPredictionData.remedy}\n` +
                         `🎬 *സിനിമാ കഥാപാത്രം:* ${currentPredictionData.movie_character}\n` +
                         `🍲 *ഭാഗ്യ ഭക്ഷണം:* ${currentPredictionData.lucky_food}\n\n` +
                         `😂 100% അശാസ്ത്രീയം, 0% ഗ്യാരണ്ടി! നിങ്ങളുടെ പ്രവചനം അറിയാൻ ഇപ്പോൾ തന്നെ സന്ദർശിക്കൂ!`;
            
            const shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
            window.open(shareUrl, "_blank");
        });
    }

    // "ശബ്ദത്തിൽ കേൾക്കൂ" (SpeechSynthesis)
    if (speakBtn) {
        speakBtn.addEventListener("click", () => {
            if (!currentPredictionData) return;
            if (!("speechSynthesis" in window)) {
                alert("നിങ്ങളുടെ ബ്രൗസറിൽ ഓഡിയോ സപ്പോർട്ട് ലഭ്യമല്ല!");
                return;
            }

            window.speechSynthesis.cancel(); // Stop any ongoing speech

            const speechText = `${currentPredictionData.name}. കേശുവിന്റെ പ്രവചനം ഇതാ: ${currentPredictionData.prediction}. പരിഹാരം: ${currentPredictionData.remedy}`;
            const utterance = new SpeechSynthesisUtterance(speechText);
            utterance.rate = 0.9;
            utterance.pitch = 1.05;

            // Attempt to find Malayalam or Indian English voice
            const voices = window.speechSynthesis.getVoices();
            const malVoice = voices.find(v => v.lang.includes("ml") || v.lang.includes("Malayalam") || v.lang.includes("en-IN"));
            if (malVoice) {
                utterance.voice = malVoice;
            }

            speakBtn.textContent = "🔊 വായിക്കുന്നു...";
            utterance.onend = () => {
                speakBtn.textContent = "🗣️ ശബ്ദത്തിൽ കേൾക്കൂ";
            };
            utterance.onerror = () => {
                speakBtn.textContent = "🗣️ ശബ്ദത്തിൽ കേൾക്കൂ";
            };

            window.speechSynthesis.speak(utterance);
        });
    }

    // "ജാതകം പ്രിന്റ് ചെയ്യൂ" (Print Slip)
    if (printBtn) {
        printBtn.addEventListener("click", () => {
            window.print();
        });
    }

    // Confetti Engine
    function launchConfetti() {
        if (!confettiCanvas) return;
        const ctx = confettiCanvas.getContext("2d");
        confettiCanvas.width = window.innerWidth;
        confettiCanvas.height = window.innerHeight;

        const particles = [];
        const colors = ["#ffcc00", "#ff007f", "#00e5ff", "#2ecc71", "#ff9900", "#9c27b0", "#ffffff"];

        for (let i = 0; i < 90; i++) {
            particles.push({
                x: window.innerWidth / 2,
                y: window.innerHeight / 2 + 100,
                radius: Math.random() * 6 + 4,
                color: colors[Math.floor(Math.random() * colors.length)],
                vx: (Math.random() - 0.5) * 16,
                vy: (Math.random() - 0.7) * 18,
                gravity: 0.35,
                rotation: Math.random() * 360,
                rotationSpeed: (Math.random() - 0.5) * 10,
                opacity: 1
            });
        }

        let animationFrame;
        function render() {
            ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
            let activeCount = 0;

            particles.forEach(p => {
                p.x += p.vx;
                p.y += p.vy;
                p.vy += p.gravity;
                p.rotation += p.rotationSpeed;
                p.opacity -= 0.012;

                if (p.opacity > 0) {
                    activeCount++;
                    ctx.save();
                    ctx.globalAlpha = p.opacity;
                    ctx.translate(p.x, p.y);
                    ctx.rotate((p.rotation * Math.PI) / 180);
                    ctx.fillStyle = p.color;
                    ctx.fillRect(-p.radius, -p.radius, p.radius * 2, p.radius * 2);
                    ctx.restore();
                }
            });

            if (activeCount > 0) {
                animationFrame = requestAnimationFrame(render);
            } else {
                ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
                cancelAnimationFrame(animationFrame);
            }
        }

        render();
    }

    // Offline / Fallback generator if network issues occur
    function getOfflinePrediction(name) {
        return {
            name: name,
            title: `ശ്രീ/ശ്രീമതി ${name} അവരുടെ അത്ഭുത ജാതകം 📜`,
            tagline: "കട്ടിൽ മഹാരാജയോഗം!",
            prediction: "നിങ്ങളുടെ ഗ്രഹനില പരിശോധിച്ചതിൽ അടുത്ത 24 മണിക്കൂറിനുള്ളിൽ ഫോൺ ചാർജ് 1% ആകും, എന്നാൽ ചാർജർ കുത്താൻ അതിയായ മടി തോന്നും!",
            accuracy: "100% അശാസ്ത്രീയം",
            dosham: "റീൽസ് അഡിക്ഷൻ കണ്ടകശനി",
            dosham_desc: "രാത്രി 2 മണി വരെ ഇൻസ്റ്റാഗ്രാമിൽ കിടന്നു കറങ്ങുന്ന അവസ്ഥ.",
            remedy: "ഉടൻ തന്നെ അടുത്തുള്ള ചായക്കടയിൽ പോയി സുഹൃത്തുക്കൾക്ക് ചൂടുള്ള പഴംപൊരിയും ചായയും വാങ്ങി കൊടുക്കുക.",
            lucky_number: "420",
            lucky_color: "കട്ടൻ ചായ കളർ ☕",
            lucky_food: "പൊറോട്ട & ബീഫ് ഫ്രൈ 🌯",
            best_career: "കവലയിലെ രാഷ്ട്രീയ നിരീക്ഷകൻ 🎙️",
            movie_character: "ദശമൂലം ദാമു",
            movie_dialogue: "കോൺഫിഡൻസ് അൺലിമിറ്റഡ്, പ്ലാനിംഗ് സീറോ! 😂",
            keshu_quote: "“ജാതകം നോക്കി പേടിക്കേണ്ട, ജീവിച്ചു പേടിച്ചാൽ മതി!” — കേശു സ്വാമി"
        };
    }
});
