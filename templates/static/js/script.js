document.addEventListener("DOMContentLoaded", function () {

    /*
    ==========================================
    INPUT PAGE
    ==========================================
    */

    const astroForm = document.getElementById("astroForm");

    if (astroForm) {

        astroForm.addEventListener("submit", function (event) {

            event.preventDefault();

            const name =
                document.getElementById("name").value.trim();

            const dob =
                document.getElementById("dob").value;

            const nakshatram =
                document.getElementById("nakshatram").value;


            if (!name || !dob || !nakshatram) {

                alert(
                    "ദയവായി എല്ലാം fill ചെയ്യൂ... നക്ഷത്രം പോലും ഒഴിവാക്കരുത്! 😂"
                );

                return;

            }


            /*
            Save user information temporarily.
            */

            localStorage.setItem(
                "keshavanName",
                name
            );

            localStorage.setItem(
                "keshavanDob",
                dob
            );

            localStorage.setItem(
                "keshavanNakshatram",
                nakshatram
            );


            /*
            Go to prediction page.
            */

            window.location.href = "/prediction";

        });

    }


    /*
    ==========================================
    PREDICTION PAGE
    ==========================================
    */

    const predictionContent =
        document.getElementById("predictionContent");


    if (predictionContent) {

        const name =
            localStorage.getItem("keshavanName")
            || "Unknown Superstar";


        const nakshatram =
            localStorage.getItem("keshavanNakshatram")
            || "Mystery Nakshatram";


        const dob =
            localStorage.getItem("keshavanDob")
            || "";


        /*
        Movie characters.
        */

        const characters = {

            Ashwathi:
                "Dashamoolam Damu — confidence unlimited, common sense optional 😂",

            Bharani:
                "Manavalan — mass undu, plan illa 😎",

            Karthika:
                "CID Unnikrishnan — investigation എല്ലാം ചെയ്യും, സ്വന്തം life മാത്രം solve ചെയ്യില്ല 🕵️",

            Rohini:
                "Ramanan — love undu, response illa 💔",

            Makayiram:
                "Dasan & Vijayan combo — ideas 100, execution 0 😂",

            Thiruvathira:
                "Aadu Thoma — life-il entry mass, exit confusion 🔥",

            Punartham:
                "Chacko — advice കൊടുക്കാൻ PhD, സ്വന്തം life-il arrears 😂",

            Pooyam:
                "Jagathy-style side character — scene ഇല്ലെങ്കിലും commentary full!",

            Ayilyam:
                "Pottan — എല്ലാം അറിയാം എന്ന് കരുതും, ഒന്നും അറിയില്ല 😭",

            Makam:
                "Rajamanikyam — style full, bank balance ചോദിക്കരുത് 💰",

            Pooram:
                "Mammootty mass hero — mirror നോക്കുമ്പോൾ തന്നെ background music കേൾക്കും 😎",

            Uthram:
                "Mohanlal protagonist — പ്രശ്നം വന്നാൽ ആദ്യം ചിരിക്കും, പിന്നെ നോക്കും 😂",

            Atham:
                "Salim Kumar character — serious situation പോലും comedy ആക്കും!",

            Chithira:
                "Dileep movie hero — ഓരോ ദിവസവും പുതിയ പ്രശ്നം, പക്ഷേ somehow survive ചെയ്യും 😂",

            Chothi:
                "Kunjiramayanam character — logic ഇല്ലെങ്കിലും confidence maximum!",

            Vishakham:
                "Inspector Balram — attitude 100%, actual progress pending 🚨",

            Anizham:
                "Pranchiyettan — വലിയ സ്വപ്നങ്ങൾ, ചെറിയ execution 😂",

            Thrikketta:
                "Thilakan-style strict character — എല്ലാവർക്കും advice, സ്വന്തം life pending!",

            Moolam:
                "Mannar Mathai — chaos follows you like background music 😂",

            Pooradam:
                "Georgekutty — plans within plans, but somehow still gets confused!",

            Uthradam:
                "Benoy — ജീവിതം serious ആക്കാൻ ശ്രമിക്കും, life തന്നെ comedy ആക്കും 😂",

            Thiruvonam:
                "Maheshinte Prathikaaram vibe — revenge later, first let's have tea ☕",

            Avittam:
                "Kattappana school hero — struggle unlimited, style questionable 😂",

            Chathayam:
                "Thondimuthal-style mastermind — ചെറിയ plan, വലിയ complications!",

            Pooruruttathi:
                "Ayyappanum Koshiyum energy — ego full tank, petrol empty 😭",

            Uthrattathi:
                "Vettam character — serious ആകാൻ ശ്രമിച്ചാലും comedy ആയിപ്പോകും 😂",

            Revathi:
                "Premam character — dreams cinematic, reality attendance shortage 💀"

        };


        const character =
            characters[nakshatram]
            || "Local Cable TV Hero — nobody knows your talent, including you 😂";


        /*
        Career predictions.
        */

        const careers = [

            "Career-il വലിയ മാറ്റം വരും... പക്ഷേ ആദ്യം Monday വരണം. ഇപ്പോൾ tea shop management ആണ് പ്രധാന priority ☕",

            "നിങ്ങൾക്ക് വലിയ potential ഉണ്ട്. അത് ഉപയോഗിക്കാത്തതിലാണ് നിങ്ങളുടെ biggest talent. Waiting for 'right time' until 2067.",

            "Corporate world നിങ്ങളെ കാത്തിരിക്കുന്നു... പക്ഷേ നിങ്ങൾ ആദ്യം 47 YouTube productivity videos കാണണം.",

            "Future-il CEO ആകാനുള്ള സാധ്യത ഉണ്ട്. CEO = Chief Excuse Officer. 😌",

            "നിങ്ങളുടെ career ഒരു Malayalam movie പോലെ ആണ് — interval വരെ ഒന്നും സംഭവിക്കില്ല.",

            "High chance of becoming an expert tea-stall reviewer. Chayaയുടെ quality കുറിച്ച് TED Talk നടത്തും.",

            "നിങ്ങളുടെ talent കണ്ടിട്ട് companies shock ആവും. Resume കണ്ടിട്ട് അതിലും വലിയ shock ആവും 😂"

        ];


        /*
        Love predictions.
        */

        const loves = [

            "Love life currently loading... 1% മുതൽ 2099 വരെ loading തന്നെ. ❤️‍🩹",

            "നിങ്ങളുടെ future partner നിങ്ങളെ കണ്ടെത്തും. പക്ഷേ Google Maps പോലും location കണ്ടെത്താൻ പറ്റുന്നില്ല.",

            "Single status വളരെ secure ആണ്. Password പോലും നിങ്ങൾക്കു മറക്കില്ല.",

            "Love വരും... knock ചെയ്യും... നിങ്ങൾ online ആയിരിക്കില്ല.",

            "Romance ഉണ്ടാകും. പക്ഷേ അത് WhatsApp status കാണുന്നതിൽ മാത്രം ഒതുങ്ങാൻ സാധ്യത കൂടുതലാണ് 😂",

            "നിങ്ങളുടെ love story-ക്ക് climax ഉണ്ടാകും. Hero ആരാണെന്ന് മാത്രം ഇതുവരെ തീരുമാനിച്ചിട്ടില്ല.",

            "Artificial Intelligence പോലും നിങ്ങളെ ghost ചെയ്യാനുള്ള സാധ്യത കാണിക്കുന്നു. 🤖💔"

        ];


        /*
        Health predictions.
        */

        const health = [

            "നിങ്ങളുടെ main exercise Instagram Reels swipe ചെയ്യുന്നതാണ്. Thumb muscle വളരെ strong ആണ്.",

            "Walking തുടങ്ങണം എന്ന് 2024 മുതൽ തീരുമാനിച്ചിരിക്കാം. Good news: തീരുമാനം ഇപ്പോഴും alive ആണ്.",

            "Future-il back pain വരാൻ സാധ്യത. കാരണം chair-നോട് ഉള്ള നിങ്ങളുടെ relationship toxic ആണ്.",

            "Fitness level: Phone battery 5% ആയാലും charger അന്വേഷിക്കാൻ എഴുന്നേൽക്കും. That's cardio.",

            "Gym membership എടുക്കും. പോകില്ല. Membership തന്നെ നിങ്ങളുടെ ഏറ്റവും consistent relationship ആയിരിക്കും.",

            "Health okay ആണ്... പക്ഷേ sleep schedule കണ്ടാൽ doctors പോലും resign ചെയ്യും 😂"

        ];


        /*
        Personality predictions.
        */

        const personalities = [

            "നിങ്ങൾ overthinking-ന്റെ unofficial brand ambassador ആണ്. ഒരു ചെറിയ message വന്നാൽ അതിന്റെ meaning 17 angle-il analyze ചെയ്യും.",

            "നിങ്ങളുടെ biggest talent unsolicited advice ആണ്. ആരും ചോദിക്കാത്ത സമയത്ത് പോലും solution ready.",

            "നിങ്ങൾക്ക് confidence ഉണ്ട്. Evidence ഇല്ല. പക്ഷേ confidence ഉണ്ട്. അതാണ് പ്രധാനപ്പെട്ടത്.",

            "നിങ്ങളുടെ life-ലെ 80% problems imagination ആണ്. ബാക്കി 20% imagination കൊണ്ടുതന്നെ solve ചെയ്യും.",

            "നിങ്ങൾ ഒരു decision എടുക്കാൻ 3 business days എടുക്കും. പിന്നെ എടുത്ത decision മാറ്റാൻ 2 minutes മാത്രം.",

            "നിങ്ങൾക്ക് വലിയ dreams ഉണ്ട്. Alarm അടിക്കുമ്പോൾ dreams-നൊപ്പം നിങ്ങൾയും snooze ചെയ്യും.",

            "നിങ്ങൾ ഒരു walking notification ആണ്. എല്ലാം അറിയണം, എല്ലാത്തിലും opinion വേണം. 😂"

        ];


        /*
        Pick random result.
        */

        function randomItem(array) {

            return array[
                Math.floor(
                    Math.random() * array.length
                )
            ];

        }


        const personality =
            randomItem(personalities);

        const career =
            randomItem(careers);

        const love =
            randomItem(loves);

        const health =
            randomItem(health);


        /*
        Greeting
        */

        document.getElementById(
            "userGreeting"
        ).innerHTML =
            `🚨 ${name}, നിങ്ങളുടെ cosmic report ready ആണ്!`;


        /*
        Movie character
        */

        document.getElementById(
            "movieCharacter"
        ).textContent =
            character;


        /*
        Small boxes
        */

        document.getElementById(
            "careerResult"
        ).textContent =
            career;


        document.getElementById(
            "loveResult"
        ).textContent =
            love;


        document.getElementById(
            "healthResult"
        ).textContent =
            health;


        /*
        Main roast paragraph
        */

        const prediction = `

            ${name}, നിങ്ങളുടെ ${nakshatram} നക്ഷത്രം
            പരിശോധിച്ചപ്പോൾ Keshavan ആദ്യം 3 തവണ കണ്ണടച്ചു.
            കാരണം ഇത്രയും confusion ഉള്ള chart
            അദ്ദേഹം ജീവിതത്തിൽ കണ്ടിട്ടില്ല. 😂

            നിങ്ങളുടെ personality നോക്കിയാൽ,
            ${personality}

            ഇപ്പോഴത്തെ ജീവിതം ഒരു Malayalam movie-യിലെ
            second half പോലെ ആണ് — എന്താണ് നടക്കുന്നതെന്ന്
            നിങ്ങൾക്കും അറിയില്ല, പക്ഷേ background-il
            dramatic music full volume.

            🎬 Movie character matching പ്രകാരം
            നിങ്ങൾക്ക് ${character} energy ആണ്.

            💼 Career:
            ${career}

            ❤️ Love Life:
            ${love}

            🏃 Health & Fitness:
            ${health}

            Future-il വലിയ കാര്യങ്ങൾ സംഭവിക്കാനുള്ള
            possibility astrology കാണിക്കുന്നുണ്ട്.
            പക്ഷേ ആദ്യം phone എടുത്ത് 6 മണിക്കൂർ
            reels കാണുന്നത് നിർത്തണം.

            അടുത്ത കുറച്ച് വർഷങ്ങളിൽ നിങ്ങൾക്ക്
            success വരും എന്നാണ് stars പറയുന്നത്.
            Stars-നെ കുറിച്ച് ഞങ്ങൾക്ക് ഒന്നും അറിയില്ല,
            പക്ഷേ അവർ അങ്ങനെ പറഞ്ഞതായി പറയാം. 😌

            ഒടുവിൽ ഒരു പ്രധാന പ്രവചനം:

            നിങ്ങളുടെ ജീവിതത്തിൽ ഒരു ദിവസം
            "ഞാൻ എന്താണ് ചെയ്യുന്നത്?"
            എന്ന ചോദ്യം വരും.

            Don't worry.

            ആ ചോദ്യത്തിന് Google പോലും answer തരില്ല. 😂😂

        `;


        document.getElementById(
            "predictionParagraph"
        ).innerHTML =
            prediction;


        /*
        Loading delay.
        */

        setTimeout(function () {

            document.getElementById(
                "loadingScreen"
            ).style.display = "none";


            document.getElementById(
                "predictionContent"
            ).classList.remove("hidden");


        }, 3000);

    }


    /*
    ==========================================
    TRY AGAIN BUTTON
    ==========================================
    */

    const tryAgain =
        document.getElementById("tryAgain");


    if (tryAgain) {

        tryAgain.addEventListener(
            "click",
            function () {

                localStorage.removeItem(
                    "keshavanName"
                );

                localStorage.removeItem(
                    "keshavanDob"
                );

                localStorage.removeItem(
                    "keshavanNakshatram"
                );


                window.location.href = "/";

            }
        );

    }

});