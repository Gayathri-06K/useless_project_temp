import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# =========================================================
# 27 MALAYALAM NAKSHATRANGAL ⭐
# =========================================================

RASHIS = [
    {
        "id": "ashwathi",
        "name": "അശ്വതി ⭐",
        "desc": "പെട്ടെന്ന് ചെയ്യും. തെറ്റും പെട്ടെന്ന്. 😂"
    },
    {
        "id": "bharani",
        "name": "ഭരണി ⭐",
        "desc": "Attitude full. Work zero. 💀"
    },
    {
        "id": "karthika",
        "name": "കാർത്തിക ⭐",
        "desc": "ചൂട് പെട്ടെന്ന്. 😂"
    },
    {
        "id": "rohini",
        "name": "രോഹിണി ⭐",
        "desc": "Style ആദ്യം. 😎"
    },
    {
        "id": "makayiram",
        "name": "മകയിരം ⭐",
        "desc": "എല്ലാം അറിയണം. 😂"
    },
    {
        "id": "thiruvathira",
        "name": "തിരുവാതിര ⭐",
        "desc": "Drama വേണം. 💀"
    },
    {
        "id": "punartham",
        "name": "പുണർതം ⭐",
        "desc": "Same mistake വീണ്ടും. 😂"
    },
    {
        "id": "pooyam",
        "name": "പൂയം ⭐",
        "desc": "Gossip വേണം. 😂"
    },
    {
        "id": "ayilyam",
        "name": "ആയില്യം ⭐",
        "desc": "Mind game pro. 💀"
    },
    {
        "id": "makam",
        "name": "മകം ⭐",
        "desc": "Boss attitude. Salary ഇല്ല. 😂"
    },
    {
        "id": "pooram",
        "name": "പൂരം ⭐",
        "desc": "Party ready. Assignment pending. 💀"
    },
    {
        "id": "uthram",
        "name": "ഉത്രം ⭐",
        "desc": "Plan ചെയ്യും. ചെയ്യില്ല. 😂"
    },
    {
        "id": "atham",
        "name": "അത്തം ⭐",
        "desc": "Overthinking pro. 💀"
    },
    {
        "id": "chithira",
        "name": "ചിത്തിര ⭐",
        "desc": "Look important. 😂"
    },
    {
        "id": "chothi",
        "name": "ചോതി ⭐",
        "desc": "Attention വേണം. 😎"
    },
    {
        "id": "vishakham",
        "name": "വിശാഖം ⭐",
        "desc": "Goal ഉണ്ട്. വഴി ഇല്ല. 😂"
    },
    {
        "id": "anizham",
        "name": "അനിഴം ⭐",
        "desc": "Advice unlimited. 💀"
    },
    {
        "id": "thrikketta",
        "name": "തൃക്കേട്ട ⭐",
        "desc": "എനിക്ക് എല്ലാം അറിയാം. 😂"
    },
    {
        "id": "moolam",
        "name": "മൂലം ⭐",
        "desc": "പ്രശ്നം വന്നാൽ ആദ്യം. 💀"
    },
    {
        "id": "pooradam",
        "name": "പൂരാടം ⭐",
        "desc": "Talk nonstop. 😂"
    },
    {
        "id": "uthradam",
        "name": "ഉത്രാടം ⭐",
        "desc": "പഠിക്കണം... ഒരിക്കൽ. 💀"
    },
    {
        "id": "thiruvonam",
        "name": "തിരുവോണം ⭐",
        "desc": "Food first. 🍗"
    },
    {
        "id": "avittam",
        "name": "അവിട്ടം ⭐",
        "desc": "Vibe മാത്രം. 🎶"
    },
    {
        "id": "chathayam",
        "name": "ചതയം ⭐",
        "desc": "Silent observer. 👀"
    },
    {
        "id": "pooruruttathi",
        "name": "പൂരുരുട്ടാതി ⭐",
        "desc": "Think. Think. Think. 💀"
    },
    {
        "id": "uthrattathi",
        "name": "ഉത്രട്ടാതി ⭐",
        "desc": "5 min rest = 5 hour sleep. 😴"
    },
    {
        "id": "revathi",
        "name": "രേവതി ⭐",
        "desc": "കാശ് വരും. പോകും. 💸"
    }
]


# =========================================================
# CHARACTER / സ്വഭാവം 😂
# =========================================================

CHARACTER = [
    "നല്ല ആളാണ്... mood അനുസരിച്ച്. 😂",
    "Confidence ഉണ്ട്. Reason ഇല്ല. 💀",
    "ചിന്തിക്കാൻ ഇഷ്ടം. Overthink ചെയ്യാൻ അതിലും ഇഷ്ടം. 😂",
    "പണി തുടങ്ങും. Finish ചെയ്യാൻ മടി. 💀",
    "പുറത്ത് calm. ഉള്ളിൽ full drama. 😂",
    "Advice കൊടുക്കും. സ്വന്തം കാര്യം മറക്കും. 💀",
    "ഉറക്കം നിങ്ങളെക്കാൾ important ആണ്. 😴",
    "ചെറിയ കാര്യം. വലിയ tension. 😂",
    "നിങ്ങൾക്ക് എല്ലാം അറിയാം... Google സമ്മതിക്കില്ല. 💀",
    "Motivation വരും. 5 മിനിറ്റിൽ പോകും. 😂",
    "Busy ആണെന്ന് പറയും. Actually reels കാണുകയാണ്. 💀",
    "Plan A മുതൽ Plan Z വരെ ഉണ്ട്. ഒന്നും നടക്കില്ല. 😂"
]


# =========================================================
# JOB / ജോലി 💼
# =========================================================

JOB = [
    "ജോലി കിട്ടും. ആദ്യം എഴുന്നേൽക്കാൻ പഠിക്കണം. 😂",
    "Career നല്ലതാണ്. Monday മോശമാണ്. 💀",
    "Promotion വരും... ഒരിക്കൽ. 😂",
    "Boss ആകും. ആദ്യം work ചെയ്യണം. 💀",
    "Interview-ൽ confidence കാണിക്കും. Answer പിന്നെ നോക്കാം. 😂",
    "ജോലി കിട്ടും. Salary കണ്ടാൽ സന്തോഷിക്കും. 💸",
    "Future-ൽ വലിയ position. ഇപ്പോൾ attendance നോക്ക്. 😂",
    "Work ചെയ്യാൻ കഴിയും. Mood വേണം. 💀",
    "Career bright ആണ്. Sleep schedule dark ആണ്. 😂",
    "ജോലി വരും. 'നാളെ തുടങ്ങാം' നിർത്തിയാൽ മതി. 💀",
    "Office-ൽ work ചെയ്യും. Lunch break-ൽ കൂടുതൽ enthusiasm. 😂",
    "Career വളരും. ആദ്യം phone താഴെ വെക്കൂ. 💀"
]


# =========================================================
# MONEY / സാമ്പത്തികം 💸
# =========================================================

MONEY = [
    "പണം വരും. ഉടനെ പോകും. 💸",
    "Wallet-ന് നിങ്ങളോട് പരാതിയുണ്ട്. 😂",
    "Salary വരും. Screenshot എടുക്കും. പിന്നെ തീരും. 💀",
    "Save ചെയ്യണം എന്ന് വിചാരിക്കും. Shopping തുറക്കും. 😂",
    "Money luck ഉണ്ട്. Saving luck ഇല്ല. 💸",
    "Cash കുറവ്. Plans കൂടുതൽ. 💀",
    "പണം കിട്ടും. എവിടെ പോയെന്ന് അറിയില്ല. 😂",
    "Wallet ഇപ്പോൾ diet-ലാണ്. 💀",
    "Future rich ആണ്. Present broke ആണ്. 😂",
    "Bank balance നോക്കരുത്. സന്തോഷം പോകും. 💀",
    "Discount കണ്ടാൽ budget മറക്കും. 😂",
    "പണം വരും. Amazon ആദ്യം അറിയും. 💸"
]


# =========================================================
# LOVE / പ്രണയം ❤️
# =========================================================

LOVE = [
    "Crush ഉണ്ടാകും. പറയാൻ ധൈര്യം ഉണ്ടാകില്ല. 😂",
    "Love വരും. Reply കിട്ടുമോ എന്നത് സംശയം. 💀",
    "ഒരു ആളെ ഇഷ്ടപ്പെടും. അയാൾക്ക് അറിയില്ല. 😂",
    "Love life-ൽ twist ഉണ്ട്. Netflix പോലും jealous. 💀",
    "Reply കാത്തിരിക്കും. Seen നോക്കി ഇരിക്കും. 😂",
    "Love luck ഉണ്ട്. Timing ഇല്ല. 💀",
    "Crush നിങ്ങളെ നോക്കും. എന്തിനെന്ന് അറിയില്ല. 😂",
    "Love story തുടങ്ങും... typing മുതൽ. 💀",
    "നിങ്ങൾ sincere ആണ്. Overthinking ആണ് villain. 😂",
    "പ്രണയം വരും. Assignment പോലെ deadline ഇല്ല. 💀",
    "Reply 'ok' ആയിരിക്കും. നിങ്ങൾ അതിന്റെ meaning അന്വേഷിക്കും. 😂",
    "Love life complicated ആണ്. നിങ്ങൾ തന്നെ simplify ചെയ്യണം. 💀"
]


# =========================================================
# MARRIAGE / വിവാഹം 💍
# =========================================================

MARRIAGE = [
    "വിവാഹം നടക്കും. Date കേശവേട്ടന് അറിയില്ല. 😂",
    "Partner കിട്ടും. ആദ്യം നിങ്ങളെ സഹിക്കണം. 💀",
    "വിവാഹം നല്ലതാകും. Remote ആരുടെ കൈയിൽ എന്നത് കണ്ടറിയാം. 😂",
    "വീട്ടുകാർക്ക് ഒരു ദിവസം സന്തോഷം വരും. 💀",
    "Marriage luck ഉണ്ട്. തീരുമാനം slow ആണ്. 😂",
    "Partner നല്ല ആളായിരിക്കും. നിങ്ങളെക്കുറിച്ച് ഉറപ്പില്ല. 💀",
    "വിവാഹം നടക്കും. Phone കുറച്ച് താഴെ വെക്കണം. 😂",
    "Love → Marriage ആകാം. Parents → Drama ആകാം. 💀",
    "വിവാഹശേഷം സമാധാനം കിട്ടും... ചിലപ്പോൾ. 😂",
    "കല്യാണം നടക്കും. ആദ്യം budget നോക്കണം. 💸",
    "Partner നിങ്ങളെ മനസ്സിലാക്കും. നിങ്ങൾ കേൾക്കുമോ എന്നതാണ് പ്രശ്നം. 😂",
    "കല്യാണം ഉറപ്പ്. Date മാത്രം suspense. 💀"
]


# =========================================================
# FUTURE / ഭാവി 🔮
# =========================================================

FUTURE = [
    "Future bright ആണ്. Curtain തുറക്കൂ. 😂",
    "വലിയ മാറ്റം വരും. Haircut ആകാം. 💀",
    "നല്ല ദിവസം വരും. അലാറം കേട്ട് എഴുന്നേൽക്കണം. 😂",
    "Success വരും. Shortcut ഇല്ല. 💀",
    "Future നല്ലതാണ്. Present ഒന്ന് ശരിയാക്കൂ. 😂",
    "ഒരു അവസരം വരും. 'നാളെ നോക്കാം' പറയരുത്. 💀",
    "യാത്രകൾ ഉണ്ടാകും. Wallet കരയും. 💸",
    "നല്ല സമയം വരും. Assignment ആദ്യം തീർക്കൂ. 😂",
    "ജീവിതത്തിൽ വലിയ twist ഉണ്ട്. 💀",
    "Future കിടിലം. Laziness ആണ് പ്രശ്നം. 😂",
    "നിങ്ങളുടെ future-ൽ success ഉണ്ട്. Alarm കേൾക്കാത്തത് മാത്രം പ്രശ്നം. 💀",
    "ഒരു ദിവസം നിങ്ങൾ famous ആകും. കാരണം എന്താണെന്ന് അറിയില്ല. 😂"
]


# =========================================================
# WARNING / ശ്രദ്ധിക്കുക ⚠️
# =========================================================

WARNING = [
    "രാത്രി 2 മണിക്ക് decisions എടുക്കരുത്. 😂",
    "ഒരു reel കൂടി = രാവിലെ. 💀",
    "Friend-ന് പണം കൊടുക്കുമ്പോൾ goodbye പറയുക. 😂",
    "Exam-ന്റെ തലേദിവസം പഠിക്കരുത്... വളരെ late ആണ്. 💀",
    "Online shopping ശ്രദ്ധിക്കുക. Wallet കരയും. 😂",
    "Alarm വെച്ചിട്ട് phone കൈയിൽ പിടിക്കരുത്. 😴",
    "Overthinking കുറയ്ക്കുക. 'OK' എല്ലായ്പ്പോഴും breakup അല്ല. 😂",
    "നാളെ മുതൽ എന്നത് cancel ചെയ്യുക. 💀",
    "Food order ചെയ്യുന്നതിന് മുമ്പ് balance നോക്കൂ. 🍗",
    "Attendance കുറവാണെങ്കിൽ ഗ്രഹങ്ങളെ കുറ്റം പറയരുത്. 😂",
    "Password friends-ന് കൊടുക്കരുത്. 💀",
    "Phone ഒന്ന് താഴെ വെക്കൂ. അതും ജീവിക്കും. 😂",
    "Exam hall-ൽ astrology work ചെയ്യില്ല. പഠിക്കണം. 💀",
    "ഒരു episode കൂടി എന്ന് പറഞ്ഞാൽ season തീരും. 😂"
]


# =========================================================
# KESHUNTE FINAL ROAST 😂
# =========================================================

KESHOO_QUOTES = [
    "പ്രശ്നം ഗ്രഹങ്ങളിൽ അല്ല... നിന്നിലാണ്! 😂",
    "കേശവേട്ടൻ നോക്കി. കേശവേട്ടൻ പോയി. 💀",
    "നിന്റെ future കണ്ടിട്ട് ഞാനും confused! 😂",
    "ഭാഗ്യം നിന്നെ block ചെയ്തിട്ടില്ല. 💀",
    "കവടി പോലും നിന്നെ കണ്ടിട്ട് ചിരിച്ചു. 😂",
    "നിന്റെ ജീവിതം comedy തന്നെ. 💀",
    "ഗ്രഹങ്ങൾ പറഞ്ഞു: 'ഇവനെ വിട്ടേക്ക്!' 😂",
    "Luck ഇപ്പോൾ airplane mode-ലാണ്. ✈️",
    "ജാതകം നല്ലതാണ്. Execution ഇല്ല. 💀",
    "നിന്നെ രക്ഷിക്കാൻ overtime വേണം! 😂",
    "Future ഉണ്ട്. ആദ്യം present ശരിയാക്ക്. 💀",
    "ഇത് പ്രവചനം അല്ല... complaint report ആണ്! 😂",
    "നിന്റെ ജാതകം വായിക്കാൻ calculator പോലും resign ചെയ്തു. 💀",
    "കേശവേട്ടൻ പറഞ്ഞു: 'ഇവന് advice കൊണ്ട് കാര്യമില്ല!' 😂",
    "ഗ്രഹങ്ങൾ meeting നടത്തി. നിന്നെ ഒഴിവാക്കി. 💀",
    "നിന്റെ luck loading ആണ്... 99%ൽ stuck. 😂"
]


# =========================================================
# MALAYALAM MOVIE CHARACTERS 🎬
# =========================================================

MOVIE_CHARACTERS = [

    {
        "character": "ദാസൻ",
        "movie": "നാടോടിക്കാറ്റ്",
        "prediction": "പ്ലാൻ ഒരുപാട്. നടക്കുന്നത് ഒന്നും ഇല്ല. 😂"
    },

    {
        "character": "വിജയൻ",
        "movie": "നാടോടിക്കാറ്റ്",
        "prediction": "പ്രശ്നം വന്നാൽ ആദ്യം പേടിക്കും. പിന്നെ solution അന്വേഷിക്കും. 💀"
    },

    {
        "character": "അപ്പുക്കുട്ടൻ",
        "movie": "ഇൻ ഹരിഹർ നഗർ",
        "prediction": "ചെറിയ പ്രശ്നം പോലും വലിയ disaster ആക്കും. 😂"
    },

    {
        "character": "മഹാദേവൻ",
        "movie": "ഇൻ ഹരിഹർ നഗർ",
        "prediction": "Leader ആണെന്ന് വിചാരിക്കും. ആരും കേൾക്കില്ല. 💀"
    },

    {
        "character": "തോമസ് കുട്ടി",
        "movie": "ഇൻ ഹരിഹർ നഗർ",
        "prediction": "പണം കണ്ടാൽ friendship മറക്കും. 💸"
    },

    {
        "character": "മൂസ",
        "movie": "CID Moosa",
        "prediction": "Plan ഒന്നുമില്ല. Confidence മാത്രം unlimited. 😂"
    },

    {
        "character": "ദിലീപ്",
        "movie": "CID Moosa",
        "prediction": "Investigation ചെയ്യും. അവസാനം സ്വയം confused ആകും. 💀"
    },

    {
        "character": "രമണൻ",
        "movie": "പഞ്ചാബി ഹൗസ്",
        "prediction": "Direction ഇല്ല. Attitude ഉണ്ട്. 😂"
    },

    {
        "character": "ഉണ്ണി",
        "movie": "പഞ്ചാബി ഹൗസ്",
        "prediction": "പ്രശ്നത്തിൽ നിന്ന് ഓടും. പ്രശ്നം പിന്നാലെ വരും. 💀"
    },

    {
        "character": "മണവാളൻ",
        "movie": "വെള്ളിമൂങ്ങ",
        "prediction": "എല്ലാം അറിയാം. സ്വന്തം life മാത്രം അറിയില്ല. 😂"
    },

    {
        "character": "ജിബി",
        "movie": "വെള്ളിമൂങ്ങ",
        "prediction": "എല്ലാവരോടും നല്ല ബന്ധം. സ്വന്തം കാര്യത്തിൽ confusion. 💀"
    },

    {
        "character": "കുഞ്ഞിരാമൻ",
        "movie": "കുഞ്ഞിരാമായണം",
        "prediction": "Love, confusion, comedy — എല്ലാം ഒരുമിച്ച്. 😂"
    },

    {
        "character": "പ്യാരിലാൽ",
        "movie": "കുഞ്ഞിരാമായണം",
        "prediction": "ചെറിയ കാര്യം വലിയ പ്രശ്നമാക്കുന്നതിൽ expert. 💀"
    },

    {
        "character": "രാജമാണിക്യം",
        "movie": "രാജമാണിക്യം",
        "prediction": "Style ഉണ്ട്. Dialogue അതിലും കൂടുതൽ. 😎"
    },

    {
        "character": "ബാലൻ",
        "movie": "തുറുപ്പുഗുലാൻ",
        "prediction": "പ്രശ്നം വന്നാൽ ആദ്യം ചിരിക്കും. പിന്നെ പണി കൊടുക്കും. 😂"
    },

    {
        "character": "മാധവൻ",
        "movie": "മീശ മാധവൻ",
        "prediction": "Innocent face. Dangerous plans. 💀"
    },

    {
        "character": "പ്രാഞ്ചിയേട്ടൻ",
        "movie": "പ്രാഞ്ചിയേട്ടൻ & ദി സെയിന്റ്",
        "prediction": "പേര് വലിയതാണ്. Achievement pending ആണ്. 😂"
    },

    {
        "character": "അച്ചുവേട്ടൻ",
        "movie": "അച്ചുവിന്റെ അമ്മ",
        "prediction": "Advice കേൾക്കും. ചെയ്യുന്നത് സ്വന്തം ഇഷ്ടം. 💀"
    },

    {
        "character": "ജോജി",
        "movie": "ജോജി",
        "prediction": "Plan മനസ്സിൽ മാത്രം. Reality വേറെ level. 😂"
    },

    {
        "character": "സക്കറിയ",
        "movie": "സാൾട്ട് ആൻഡ് പെപ്പർ",
        "prediction": "Food കണ്ടാൽ എല്ലാ problems-ും മറക്കും. 🍗"
    },

    {
        "character": "ബാബുരാജ്",
        "movie": "സാൾട്ട് ആൻഡ് പെപ്പർ",
        "prediction": "Food + attitude = നിങ്ങൾ. 😂"
    },

    {
        "character": "വിനോദ്",
        "movie": "തട്ടത്തിൻ മറയത്ത്",
        "prediction": "Crush കണ്ടാൽ brain പോകും. 💀"
    },

    {
        "character": "ലാലപ്പൻ",
        "movie": "തട്ടത്തിൻ മറയത്ത്",
        "prediction": "Love advice കൊടുക്കും. സ്വന്തം love life disaster. 😂"
    },

    {
        "character": "തൊമ്മൻ",
        "movie": "തൊമ്മനും മക്കളും",
        "prediction": "Plan simple. Execution dangerous. 💀"
    },

    {
        "character": "വാസു",
        "movie": "ചോട്ടാ മുംബൈ",
        "prediction": "എന്ത് സംഭവിച്ചാലും കൂടെ നിൽക്കും. 😂"
    },

    {
        "character": "മൊട്ട",
        "movie": "ചോട്ടാ മുംബൈ",
        "prediction": "എന്ത് സംഭവിച്ചാലും ഭക്ഷണം ആദ്യം. 🍗"
    },

    {
        "character": "പട്ടാഭിരാമൻ",
        "movie": "ചോട്ടാ മുംബൈ",
        "prediction": "Gang-ൽ ഉണ്ടാകും. Work ചെയ്യില്ല. 💀"
    },

    {
        "character": "നിശ്ചൽ",
        "movie": "കിലുക്കം",
        "prediction": "Situation എന്തായാലും comedy ഉണ്ടാക്കും. 😂"
    },

    {
        "character": "ജഗതി",
        "movie": "കിലുക്കം",
        "prediction": "സംസാരം തുടങ്ങിയാൽ stop button കാണില്ല. 💀"
    },

    {
        "character": "അനന്തൻ നമ്പ്യാർ",
        "movie": "വിയറ്റ്നാം കോളനി",
        "prediction": "എല്ലാം control ചെയ്യാം എന്ന് കരുതും. 😂"
    },

    {
        "character": "കുഞ്ഞിക്കൂനൻ",
        "movie": "കുഞ്ഞിക്കൂനൻ",
        "prediction": "Life serious ആണ്. Luck അതിലും serious. 💀"
    },

    {
        "character": "ശശി",
        "movie": "നരസിംഹം",
        "prediction": "Dialogue പറയാൻ അവസരം കിട്ടിയാൽ വിടില്ല. 😎"
    },

    {
        "character": "തിലകൻ",
        "movie": "സ്പടികം",
        "prediction": "ഒരു തീരുമാനം എടുത്താൽ പിന്നെ മാറ്റില്ല. 💀"
    },

    {
        "character": "അജയൻ",
        "movie": "അവതാരം",
        "prediction": "Justice വേണം. ആദ്യം സ്വന്തം life നോക്ക്. 😂"
    }
]


# =========================================================
# GREETINGS 🔮
# =========================================================

def get_greeting(name):

    greetings = [
        f"എടാ {name}, കൈ ഒന്ന് കാണിക്കൂ... 🔮",
        f"{name}, കേശവേട്ടൻ നിന്റെ future നോക്കി! 😂",
        f"ദേ {name}, ഇനി സത്യം കേൾക്കണം! 💀",
        f"{name}, നിന്റെ നക്ഷത്രം കണ്ടപ്പോൾ കേശവേട്ടൻ ഞെട്ടി! 😂",
        f"അല്ലയോ {name}, എന്തൊക്കെയാ ഈ കൈരേഖ! 💀",
        f"{name}, ഇനി പറയുന്നത് കേട്ട് കരയരുത്! 😂",
        f"എടാ {name}, നിന്റെ future തുറന്നുനോക്കാം! 🔮",
        f"{name}, കേശവേട്ടന് എല്ലാം മനസ്സിലായി! 💀",
        f"{name}, കവടി ready ആണ്! 😂",
        f"ദേ {name}, ഗ്രഹങ്ങൾ complaint കൊടുത്തിട്ടുണ്ട്! 💀"
    ]

    return random.choice(greetings)


# =========================================================
# FIND NAKSHATRAM
# =========================================================

def get_rashi(rashi_id):

    for rashi in RASHIS:

        if rashi["id"] == rashi_id:
            return rashi

    return None


# =========================================================
# GENERATE FULL PREDICTION
# =========================================================

def generate_prediction(name="സുഹൃത്തേ", rashi_id=None):

    name = str(name).strip()

    if not name:
        name = "സുഹൃത്തേ"

    selected_rashi = get_rashi(rashi_id)

    movie_character = random.choice(MOVIE_CHARACTERS)

    return {

        "name": name,

        "greeting": get_greeting(name),

        "rashi": (
            selected_rashi["name"]
            if selected_rashi
            else "നക്ഷത്രം അറിയില്ല ⭐"
        ),

        "rashi_desc": (
            selected_rashi["desc"]
            if selected_rashi
            else "കേശവേട്ടന് പോലും അറിയില്ല! 😂"
        ),

        "character": random.choice(CHARACTER),

        "job": random.choice(JOB),

        "money": random.choice(MONEY),

        "love": random.choice(LOVE),

        "marriage": random.choice(MARRIAGE),

        "future": random.choice(FUTURE),

        "warning": random.choice(WARNING),

        "keshoo_quote": random.choice(KESHOO_QUOTES),

        # Movie character
        "movie_character": movie_character["character"],

        "movie_movie": movie_character["movie"],

        "movie_prediction": movie_character["prediction"],

        # Random scores
        "luck_score": random.randint(1, 100),

        "danger_score": random.randint(1, 100)
    }


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        rashis=RASHIS
    )


# =========================================================
# PREDICTION API
# =========================================================

@app.route("/api/predict", methods=["GET", "POST"])
def api_predict():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        name = data.get(
            "name",
            "സുഹൃത്തേ"
        )

        rashi_id = data.get("rashi")

    else:

        name = request.args.get(
            "name",
            "സുഹൃത്തേ"
        )

        rashi_id = request.args.get("rashi")

    result = generate_prediction(
        name=name,
        rashi_id=rashi_id
    )

    return jsonify(result)


# =========================================================
# PORUTHAM ❤️
# =========================================================

@app.route("/api/porutham", methods=["GET", "POST"])
def porutham():

    if request.method == "POST":

        data = request.get_json(silent=True) or {}

        name1 = data.get(
            "name1",
            "ഒരാൾ"
        )

        name2 = data.get(
            "name2",
            "മറ്റൊരാൾ"
        )

    else:

        name1 = request.args.get(
            "name1",
            "ഒരാൾ"
        )

        name2 = request.args.get(
            "name2",
            "മറ്റൊരാൾ"
        )

    compatibility = [

        {
            "percentage": "8%",
            "title": "പൊട്ടക്കിണർ കോംബോ! 😂",
            "text": (
                f"{name1} + {name2} = "
                "ഒരുമിച്ച് project ചെയ്താൽ project തന്നെ കരയും! 💀"
            )
        },

        {
            "percentage": "98%",
            "title": "റീൽസ് സോൾമേറ്റ്സ്! 📱",
            "text": (
                f"{name1} reel അയക്കും. "
                f"{name2} reply ചെയ്യും. "
                "പിന്നെ രണ്ടുപേരും 3 മണിക്കൂർ scroll ചെയ്യും! 😂"
            )
        },

        {
            "percentage": "42%",
            "title": "കടം വാങ്ങുന്ന കൂട്ടുകെട്ട്! 💸",
            "text": (
                f"{name1} ₹50 ചോദിക്കും. "
                f"{name2} കൊടുക്കും. "
                "തിരിച്ചു കിട്ടില്ല! 💀"
            )
        },

        {
            "percentage": "15%",
            "title": "സപ്ലി കൂട്ടുകെട്ട്! 📚",
            "text": (
                f"{name1} പഠിക്കില്ല. "
                f"{name2} പഠിക്കില്ല. "
                "Result രണ്ടുപേരും നോക്കും! 😂"
            )
        },

        {
            "percentage": "100%",
            "title": "രണ്ടുപേരും ഒരേ ദുരന്തം! 😂",
            "text": (
                f"{name1}യും {name2}യും കൂടിയാൽ "
                "ചുറ്റുമുള്ളവർക്ക് പണി! 💀"
            )
        },

        {
            "percentage": "69%",
            "title": "കട്ടൻ ചായ കോംബോ! ☕",
            "text": (
                f"{name1} ചായ വാങ്ങും. "
                f"{name2} കുടിക്കും. "
                "Bill ആരും കൊടുക്കില്ല! 😂"
            )
        },

        {
            "percentage": "1%",
            "title": "Worst Combo 💀",
            "text": (
                f"{name1}യും {name2}യും ഒരുമിച്ചാൽ "
                "കേശവേട്ടൻ പോലും ഓടും! 😂"
            )
        },

        {
            "percentage": "87%",
            "title": "Late Legends ⏰",
            "text": (
                f"{name1} late. "
                f"{name2} അതിലും late. "
                "Class തീരും! 😂"
            )
        },

        {
            "percentage": "73%",
            "title": "Food Partners 🍗",
            "text": (
                f"{name1} food കാണും. "
                f"{name2} order ചെയ്യും. "
                "Diet പോയി! 😂"
            )
        },

        {
            "percentage": "91%",
            "title": "Overthinking Couple 💀",
            "text": (
                f"{name1} 'hmm' അയക്കും. "
                f"{name2} അതിന്റെ meaning അന്വേഷിക്കും. 😂"
            )
        },

        {
            "percentage": "67%",
            "title": "Assignment Partners 📚",
            "text": (
                f"{name1} assignment മറക്കും. "
                f"{name2}യും മറക്കും. "
                "Teacher മാത്രം ഓർക്കും! 💀"
            )
        },

        {
            "percentage": "99%",
            "title": "Sleep Partners 😴",
            "text": (
                f"{name1} ഉറങ്ങും. "
                f"{name2} ഉറങ്ങും. "
                "Plan cancel ചെയ്യും! 😂"
            )
        }
    ]

    result = random.choice(compatibility)

    return jsonify({

        "name1": name1,

        "name2": name2,

        "percentage": result["percentage"],

        "title": result["title"],

        "text": result["text"]
    })


# =========================================================
# PREDICTION PAGE
# =========================================================

@app.route("/prediction", methods=["GET", "POST"])
def prediction():

    if request.method == "POST":

        data = request.form

        name = data.get(
            "name",
            "സുഹൃത്തേ"
        )

        rashi_id = data.get("rashi")

    else:

        name = request.args.get(
            "name",
            "സുഹൃത്തേ"
        )

        rashi_id = request.args.get("rashi")

    result = generate_prediction(
        name=name,
        rashi_id=rashi_id
    )

    return render_template(

        "index.html",

        rashis=RASHIS,

        initial_result=result
    )


# =========================================================
# RUN FLASK 🚀
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )