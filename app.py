"""
Keshunte Pravajanam (കേശുവിന്റെ പ്രവചനം)
Flask Backend Application
A satirical, hilarious Malayalam astrology prediction generator
for the College Useless Project Competition.
"""

import os
import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# =========================================================
# 27 MALAYALAM NAKSHATRANGAL ⭐
# =========================================================

RASHIS = [
    {"id": "ashwathi", "name": "അശ്വതി ⭐", "desc": "പെട്ടെന്ന് ചെയ്യും. തെറ്റും പെട്ടെന്ന്. 😂"},
    {"id": "bharani", "name": "ഭരണി ⭐", "desc": "Attitude full. Work zero. 💀"},
    {"id": "karthika", "name": "കാർത്തിക ⭐", "desc": "ചൂട് പെട്ടെന്ന്. 😂"},
    {"id": "rohini", "name": "രോഹിണി ⭐", "desc": "Style ആദ്യം. 😎"},
    {"id": "makayiram", "name": "മകയിരം ⭐", "desc": "എല്ലാം അറിയണം. 😂"},
    {"id": "thiruvathira", "name": "തിരുവാതിര ⭐", "desc": "Drama വേണം. 💀"},
    {"id": "punartham", "name": "പുണർതം ⭐", "desc": "Same mistake വീണ്ടും. 😂"},
    {"id": "pooyam", "name": "പൂയം ⭐", "desc": "Gossip വേണം. 😂"},
    {"id": "ayilyam", "name": "ആയില്യം ⭐", "desc": "Mind game pro. 💀"},
    {"id": "makam", "name": "മകം ⭐", "desc": "Boss attitude. Salary ഇല്ല. 😂"},
    {"id": "pooram", "name": "പൂരം ⭐", "desc": "Party ready. Assignment pending. 💀"},
    {"id": "uthram", "name": "ഉത്രം ⭐", "desc": "Plan ചെയ്യും. ചെയ്യില്ല. 😂"},
    {"id": "atham", "name": "അത്തം ⭐", "desc": "Overthinking pro. 💀"},
    {"id": "chithira", "name": "ചിത്തിര ⭐", "desc": "Look important. 😂"},
    {"id": "chothi", "name": "ചോതി ⭐", "desc": "Attention വേണം. 😎"},
    {"id": "vishakham", "name": "വിശാഖം ⭐", "desc": "Goal ഉണ്ട്. വഴി ഇല്ല. 😂"},
    {"id": "anizham", "name": "അനിഴം ⭐", "desc": "Advice unlimited. 💀"},
    {"id": "thrikketta", "name": "തൃക്കേട്ട ⭐", "desc": "എനിക്ക് എല്ലാം അറിയാം. 😂"},
    {"id": "moolam", "name": "മൂലം ⭐", "desc": "പ്രശ്നം വന്നാൽ ആദ്യം. 💀"},
    {"id": "pooradam", "name": "പൂരാടം ⭐", "desc": "Talk nonstop. 😂"},
    {"id": "uthradam", "name": "ഉത്രാടം ⭐", "desc": "പഠിക്കണം... ഒരിക്കൽ. 💀"},
    {"id": "thiruvonam", "name": "തിരുവോണം ⭐", "desc": "Food first. 🍗"},
    {"id": "avittam", "name": "അവിട്ടം ⭐", "desc": "Vibe മാത്രം. 🎶"},
    {"id": "chathayam", "name": "ചതയം ⭐", "desc": "Silent observer. 👀"},
    {"id": "pooruruttathi", "name": "പൂരുരുട്ടാതി ⭐", "desc": "Think. Think. Think. 💀"},
    {"id": "uthrattathi", "name": "ഉത്രട്ടാതി ⭐", "desc": "5 min rest = 5 hour sleep. 😴"},
    {"id": "revathi", "name": "രേവതി ⭐", "desc": "കാശ് വരും. പോകും. 💸"}
]

# =========================================================
# HILARIOUS MALAYALAM PREDICTION DATABASE
# =========================================================

PREDICTIONS_POOL = [
    {
        "text": "നിങ്ങളുടെ ഗ്രഹനില പരിശോധിച്ചതിൽ അടുത്ത 24 മണിക്കൂറിനുള്ളിൽ ഫോൺ ചാർജ് 1% ആകും, എന്നാൽ ചാർജർ കുത്താൻ നിങ്ങൾക്ക് അതിയായ മടി തോന്നും!",
        "tagline": "മടി മഹാരാജയോഗം!",
        "accuracy": "99.9% പരാജയം"
    },
    {
        "text": "ശനി നിങ്ങളുടെ രാശിയിൽ നോക്കി അട്ടഹസിക്കുന്നു! കാരണം എന്തെന്നാൽ, പഠിക്കാൻ എടുത്തു വെച്ച ബുക്ക് തൊടാതെ നിങ്ങൾ 2 മണിക്കൂർ റീൽസ് സ്ക്രോൾ ചെയ്യും.",
        "tagline": "റീൽസ് പാരഡൈസ്!",
        "accuracy": "100% ശാസ്ത്രീയ തെളിവില്ല"
    },
    {
        "text": "വളരെ വലിയൊരു രാജയോഗം കാണുന്നുണ്ട്! പക്ഷേ ആ യോഗം അടുത്ത ജന്മത്തിലാണോ അതോ അതിനടുത്ത ജന്മത്തിലാണോ എന്നതിൽ ഗ്രഹങ്ങൾക്ക് ചെറിയ കൺഫ്യൂഷൻ ഉണ്ട്.",
        "tagline": "അടുത്ത ജന്മത്തിൽ പൊളിക്കും!",
        "accuracy": "0.01% സാധ്യത"
    },
    {
        "text": "നിങ്ങൾ അടുത്ത ആഴ്ച ഒരു കോടീശ്വരൻ ആകാൻ ചാൻസ് ഉണ്ട്... പക്ഷേ ആ സ്വപ്നത്തിന്റെ ക്ലൈമാക്സിൽ അമ്മ വന്ന് തട്ടിവിളിച്ചു ചൂലെടുക്കും!",
        "tagline": "സ്വപ്നലോകത്തെ സുൽത്താൻ!",
        "accuracy": "അമ്മയുടെ മൂഡ് അനുസരിച്ച് മാറും"
    },
    {
        "text": "ജ്യോതിഷ ശാസ്ത്ര പ്രകാരം നിങ്ങളുടെ ജീവിതത്തിലേക്ക് ഉടൻ ഒരു പ്രത്യേക വ്യക്തി കടന്നുവരും... ആ വ്യക്തി മറ്റാരുമല്ല, എക്സാം റിസൾട്ടും കൊണ്ട് വരുന്ന പ്രിൻസിപ്പൽ!",
        "tagline": "അപകട മുന്നറിയിപ്പ്!",
        "accuracy": "സത്യം മാത്രം ബോധിപ്പിക്കുന്നു"
    },
    {
        "text": "ചൊവ്വാദോഷവും രാഹുകാലവും നിങ്ങളെ കണ്ട് വഴിമാറി നടക്കുന്നു! കാരണം നിങ്ങൾ രാവിലെ എഴുന്നേൽക്കുന്ന സമയം കണ്ട് ഗ്രഹങ്ങൾ തന്നെ പേടിച്ചു പോയി.",
        "tagline": "ഉറക്കപ്രഭു യോഗം!",
        "accuracy": "സൂര്യോദയത്തിന് ശേഷം മാത്രം സാധുത"
    },
    {
        "text": "നിങ്ങൾ ഒരു ജീനിയസ് ആണ്, ലോകം അത് തിരിച്ചറിയാൻ പോകുന്നതേയുള്ളൂ... പക്ഷേ നിലവിലെ അവസ്ഥയിൽ ഉച്ചയ്ക്ക് എന്ത് കഴിക്കണം എന്ന് തീരുമാനിക്കാൻ 3 മണിക്കൂർ വേണം!",
        "tagline": "ആശയക്കുഴപ്പം അൺലിമിറ്റഡ്!",
        "accuracy": "വിശപ്പനുസരിച്ച് വ്യത്യാസപ്പെടും"
    },
    {
        "text": "നിങ്ങളുടെ കരിയർ ഒരു റോക്കറ്റ് പോലെ കുതിച്ചുയരും... പക്ഷേ നിർഭാഗ്യവശാൽ റോക്കറ്റിന് പെട്രോളില്ലാത്തതിനാൽ ലോഞ്ചിംഗ് പാഡിൽ തന്നെ കിടക്കും!",
        "tagline": "ഐഎസ്ആർഒ നോക്കി ചിരിച്ച ജാതകം!",
        "accuracy": "കട്ടൻ ചായ സാക്ഷിയായി പറയുന്നു"
    },
    {
        "text": "കൈരേഖ നോക്കിയ കേശുവിന് കണ്ണുതള്ളി! വിദേശയാത്രയ്ക്കുള്ള എല്ലാ സാധ്യതയും ഉണ്ട്... പക്ഷേ പാസ്പോർട്ട് ഇല്ലാത്തതുകൊണ്ട് ഗൂഗിൾ സ്ട്രീറ്റ് വ്യൂവിൽ കറങ്ങേണ്ടി വരും.",
        "tagline": "ഡിജിറ്റൽ പ്രവാസി!",
        "accuracy": "4G റേഞ്ച് അനുസരിച്ച് മാത്രം"
    },
    {
        "text": "നിങ്ങൾ വിചാരിച്ചാൽ ഒരു പുതിയ സ്റ്റാർട്ടപ്പ് സാമ്രാജ്യം തന്നെ ഉണ്ടാക്കാം... പക്ഷേ കട്ടിലിൽ കിടന്നുള്ള ആലോചന കഴിഞ്ഞു എഴുന്നേൽക്കാനുള്ള ആ മടി ഇല്ലേ, അതാണ് വില്ലൻ!",
        "tagline": "കട്ടിൽ ശാസ്ത്രജ്ഞൻ!",
        "accuracy": "തലയിണയുടെ ഉറപ്പ് അനുസരിച്ചിരിക്കും"
    },
    {
        "text": "നിങ്ങളുടെ ഗ്രഹനിലയിൽ പ്രണയത്തിന് സാധ്യത 100% ഉണ്ട്... പക്ഷേ മറുഭാഗത്ത് ഉള്ള ആൾ നിങ്ങളെ 'ഒരു നല്ല സുഹൃത്തായി' മാത്രമേ കാണുന്നുള്ളൂ!",
        "tagline": "ഫ്രണ്ട്‌സോൺ അമൃതം!",
        "accuracy": "ഹൃദയം തകർന്ന വാറണ്ടി"
    },
    {
        "text": "ഇന്ന് നിങ്ങൾ ചെയ്യുന്ന എല്ലാ കാര്യങ്ങളും വിജയിക്കും... ഉറങ്ങുന്നത് ഒഴികെ! കാരണം ഉറങ്ങാൻ കിടക്കുമ്പോൾ 5 വർഷം മുൻപ് പറഞ്ഞ മണ്ടത്തരങ്ങൾ ഓർമ്മ വരും.",
        "tagline": "ഓവർതിങ്കിങ് താണ്ഡവം!",
        "accuracy": "രാത്രി 2 മണിക്ക് ആക്ടീവ്"
    },
    {
        "text": "നിങ്ങൾക്ക് നാളെ ലോട്ടറി അടിക്കാൻ സാധ്യതയുണ്ട്! ടിക്കറ്റ് എടുത്തിട്ടുണ്ടെങ്കിൽ മാത്രം. ടിക്കറ്റ് എടുത്തില്ലെങ്കിലും വിഷമിക്കേണ്ട, എടുത്തവനും അടിക്കാൻ പോകുന്നില്ല!",
        "tagline": "ഭാഗ്യക്കുറി മാജിക്!",
        "accuracy": "ഭാഗ്യദേവത ലീവിലാണ്"
    },
    {
        "text": "കവടി നിരത്തി നോക്കിയപ്പോൾ കേശു കണ്ടത്: നിങ്ങൾ ഗ്രൂപ്പ് പ്രൊജക്റ്റിൽ ഒരു പണിയും എടുക്കാതെ മുഴുവൻ ക്രെഡിറ്റും വാങ്ങാൻ ജനിച്ച ആളാണ്!",
        "tagline": "പ്രോജക്ട് പരാന്നഭോജി!",
        "accuracy": "വൈവ എക്സാമിനർ അറിയാതെ നോക്കണം"
    },
    {
        "text": "നിങ്ങളുടെ ജാതകത്തിൽ ബുധൻ വളരെ ശക്തനാണ്. അതുകൊണ്ട് കോളേജിൽ വൈകി ചെന്നാലും ആരും ചോദ്യം ചെയ്യില്ല... കാരണം ക്ലാസ്സ് തുടങ്ങുന്നതിന് മുൻപ് അറ്റൻഡൻസ് തീർന്നിട്ടുണ്ടാവും!",
        "tagline": "മാസ്സ് എൻട്രി, സീറോ അറ്റൻഡൻസ്!",
        "accuracy": "കോളേജ് റൂൾസിന് അതീതം"
    }
]

DOSHAMS = [
    {"name": "റീൽസ് അഡിക്ഷൻ ദോഷം", "desc": "കണ്ണിൽ എപ്പോഴും ഫോൺ സ്ക്രീനിന്റെ നീല വെളിച്ചം അടിക്കുന്ന അവസ്ഥ."},
    {"name": "അലസതാ മഹാരാജയോഗം", "desc": "ഭൂമി കുലുങ്ങിയാലും കട്ടിലിൽ നിന്ന് താഴെ ഇറങ്ങാത്ത സ്ഥിതിവിശേഷം."},
    {"name": "ചായ കുടി ദോഷം", "desc": "കട്ടൻ ചായ കിട്ടിയില്ലെങ്കിൽ ചുറ്റുമുള്ളവരോട് തട്ടിക്കയറുന്ന ശനിദോഷം."},
    {"name": "സുഹൃത്തുക്കൾക്ക് ചായ വാങ്ങി കൊടുക്കാത്ത കണ്ടകശനി", "desc": "പഴ്സിൽ പൈസ ഉണ്ടായിട്ടും ഗൂഗിൾ പേ സെർവർ ഡൗൺ ആണെന്ന് പറയുന്ന ദോഷം."},
    {"name": "നാളെ മുതൽ പഠിക്കാം എന്ന മാന്ത്രിക ദോഷം", "desc": "സിലബസ് കാണുമ്പോൾ മാത്രം മനസ്സിന് ഉണ്ടാകുന്ന നിസ്സഹായാവസ്ഥ."},
    {"name": "വൈഫൈ റേഞ്ച് കുറയുന്ന അപൂർവ ദോഷം", "desc": "പ്രധാനപ്പെട്ട വീഡിയോ കാണുമ്പോൾ മാത്രം ബഫറിംഗ് വരുന്ന രാഹുകാലം."},
    {"name": "ഗ്രൂപ്പ് പ്രൊജക്റ്റിൽ സീൻ ഉണ്ടാക്കുന്ന ചോവ്വാദോഷം", "desc": "ഗ്രൂപ്പിൽ 'I am working on it' എന്ന് മാത്രം മെസ്സേജ് അയക്കുന്ന ദോഷം."},
    {"name": "പപ്പടം പൊട്ടിപ്പോകുന്ന നിമിഷദോഷം", "desc": "ഊണ് കഴിക്കാൻ ഇരിക്കുമ്പോൾ പപ്പടം തണുത്തു വായു പോയിരിക്കുന്ന അവസ്ഥ."}
]

REMEDIES = [
    "ഉടൻ തന്നെ അടുത്തുള്ള ചായക്കടയിൽ പോയി കൂട്ടുകാർക്ക് ചൂടുള്ള പഴംപൊരിയും ചായയും വാങ്ങി കൊടുക്കുക.",
    "തുടർച്ചയായി 15 മിനിറ്റ് ഫോൺ തൊടാതെ ഇരിക്കുക (ഇത് ചെയ്യാൻ പറ്റിയില്ലെങ്കിൽ കേശുവിനെ കുറ്റം പറയരുത്).",
    "രാവിലെ 11 മണിക്ക് മുൻപ് എഴുന്നേൽക്കാൻ നോക്കാതിരിക്കുക; ഗ്രഹങ്ങൾക്ക് അത് തീരെ ഇഷ്ടപ്പെടില്ല.",
    "ഇന്ന് വൈകുന്നേരം അടുത്ത ചങ്ങാതിക്ക് ഗൂഗിൾ പേ വഴി 50 രൂപ അയച്ചുകൊടുക്കുക, അത്യപൂർവ്വ പുണ്യം ലഭിക്കും.",
    "കണ്ണാടിയിൽ നോക്കി 'ഞാൻ ഒരു പുലിയാണ്' എന്ന് 3 പ്രാവശ്യം ഉറക്കെ പറയുക (വീട്ടുകാർ ചൂരൽ എടുക്കാതെ നോക്കുക).",
    "ഒരു പ്ലേറ്റ് ബിരിയാണി ഫുൾ ആയി കഴിച്ച് 2 മണിക്കൂർ സുഖമായി കിടന്നുറങ്ങുക; സർവ്വ ദോഷങ്ങളും പമ്പ കടക്കും.",
    "WhatsApp ഫാമിലി ഗ്രൂപ്പിൽ വരുന്ന 'Good Morning' പൂക്കളുടെ ഫോട്ടോകൾക്ക് റിപ്ലൈ കൊടുക്കാതിരിക്കുക.",
    "ഹെഡ്‌ഫോൺ വെച്ച് പാട്ട് കേൾക്കുക, ആരോടെങ്കിലും സംസാരിക്കാൻ തോന്നിയാൽ ഉടൻ വെള്ളം കുടിക്കുക."
]

LUCKY_NUMBERS = ["420", "0 (പൂജ്യം)", "99.9", "-100", "7 (തല അണ്ണൻ)", "69", "അനന്തം (Infinity)", "പരീക്ഷയുടെ പാസ് മാർക്ക്"]
LUCKY_COLORS = ["കട്ടൻ ചായ കളർ ☕", "പഴംപൊരി മഞ്ഞ 🍌", "ഹർത്താൽ കറുപ്പ് 🖤", "പച്ചമുളക് പച്ച 🌶️", "ബിരിയാണി ഓറഞ്ച് 🍛", "വൈഫൈ സിഗ്നൽ പച്ച 📶", "ചോരച്ചുവപ്പ് 🩸"]
LUCKY_FOODS = ["പൊറോട്ട & ബീഫ് ഫ്രൈ", "നെയ്‌റോസ്റ്റ് & ചമ്മന്തി", "ചൂട് പഴംപൊരി", "ദമ്പതി ബിരിയാണി", "കട്ടൻ ചായ & പരിപ്പുവട", "തട്ടുകട ദോശ"]
BEST_CAREERS = [
    "കവലയിലെ രാഷ്ട്രീയ നിരീക്ഷകൻ",
    "വാട്സാപ്പ് ഫോർവേഡ് ചീഫ് എഡിറ്റർ",
    "കട്ടിലിൽ കിടന്നു ചിന്തിക്കുന്ന ശാസ്ത്രജ്ഞൻ",
    "റീൽസ് സ്ക്രോളിംഗ് സ്പെഷ്യലിസ്റ്റ്",
    "ചായക്കട ബെഞ്ച് ഡയറക്ടർ",
    "സിലബസ് പേജ് എണ്ണുന്ന ഇൻവെസ്റ്റിഗേറ്റർ",
    "കട്ട ബോറടി അംബാസഡർ"
]

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

KESHOO_QUOTES = [
    "“ജാതകം നോക്കി പേടിക്കേണ്ട, ജീവിച്ചു പേടിച്ചാൽ മതി!” — കേശു സ്വാമി",
    "“പ്രശ്നം ഗ്രഹങ്ങളിൽ അല്ല... നിന്നിലാണ്! 😂” — കേശു",
    "“കേശവേട്ടൻ നോക്കി. കേശവേട്ടൻ പോയി. 💀” — കേശു സ്വാമി",
    "“കവടി പോലും നിന്നെ കണ്ടിട്ട് ചിരിച്ചു. 😂” — കേശു",
    "“എന്റെ പ്രവചനം തെറ്റിയാൽ നിങ്ങളുടെ ഗ്രഹങ്ങൾക്ക് എന്തോ കുഴപ്പമുണ്ട്!” — കേശു",
    "“കവടി ഒരിക്കലും കള്ളം പറയില്ല, കാരണം കവടിക്ക് സംസാരിക്കാൻ അറിയില്ലല്ലോ!” — കേശു സ്വാമി",
    "“ശനി ദോഷമല്ല പ്രശ്നം, രാവിലെ എഴുന്നേൽക്കാൻ തോന്നാത്ത മടിയാണ് മെയിൻ പ്രശ്നം!” — കേശു",
    "“നിന്റെ ജാതകം വായിക്കാൻ calculator പോലും resign ചെയ്തു. 💀” — കേശു സ്വാമി"
]

MOVIE_CHARACTERS = [
    {"character": "ദശമൂലം ദാമു", "movie": "ചട്ടമ്പിനാട്", "prediction": "കോൺഫിഡൻസ് അൺലിമിറ്റഡ്, പ്ലാനിംഗ് സീറോ! 😂"},
    {"character": "മണവാളൻ", "movie": "പുലിവാൽ കല്യാണം", "prediction": "സ്റ്റൈൽ ഫുൾ ആണ്, പക്ഷേ ബാങ്ക് അക്കൗണ്ടിൽ മിനിമം ബാലൻസ് ഇല്ല! 😎"},
    {"character": "ദാസൻ", "movie": "നാടോടിക്കാറ്റ്", "prediction": "പ്ലാൻ ഒരുപാട്. നടക്കുന്നത് ഒന്നും ഇല്ല. 😂"},
    {"character": "വിജയൻ", "movie": "നാടോടിക്കാറ്റ്", "prediction": "പ്രശ്നം വന്നാൽ ആദ്യം പേടിക്കും. പിന്നെ solution അന്വേഷിക്കും. 💀"},
    {"character": "രമണൻ", "movie": "പഞ്ചാബി ഹൗസ്", "prediction": "കഷ്ടപ്പാടും കണ്ണീരും മാത്രം ബാക്കി... മുതലാളി ശമ്പളം തരില്ല! 💔"},
    {"character": "മൂസ", "movie": "CID Moosa", "prediction": "Plan ഒന്നുമില്ല. Confidence മാത്രം unlimited. 😂"},
    {"character": "സിഐഡി ഉണ്ണികൃഷ്ണൻ", "movie": "സിഐഡി ഉണ്ണികൃഷ്ണൻ", "prediction": "നാട്ടിലെ എല്ലാ കാര്യങ്ങളും അന്വേഷിക്കും, സ്വന്തം ലൈഫ് ഒഴികെ! 🕵️"},
    {"character": "അപ്പുക്കുട്ടൻ", "movie": "ഇൻ ഹരിഹർ നഗർ", "prediction": "ചെറിയ പ്രശ്നം പോലും വലിയ disaster ആക്കും. 😂"},
    {"character": "രാജമാണിക്യം", "movie": "രാജമാണിക്യം", "prediction": "Style ഉണ്ട്. Dialogue അതിലും കൂടുതൽ. 😎"},
    {"character": "നിശ്ചൽ", "movie": "കിലുക്കം", "prediction": "Situation എന്തായാലും comedy ഉണ്ടാക്കും. 😂"}
]


def get_greeting(name):
    greetings = [
        f"എടാ {name}, കൈ ഒന്ന് കാണിക്കൂ... 🔮",
        f"{name}, കേശവേട്ടൻ നിന്റെ future നോക്കി! 😂",
        f"ദേ {name}, ഇനി സത്യം കേൾക്കണം! 💀",
        f"{name}, നിന്റെ നക്ഷത്രം കണ്ടപ്പോൾ കേശവേട്ടൻ ഞെട്ടി! 😂",
        f"അല്ലയോ {name}, എന്തൊക്കെയാ ഈ കൈരേഖ! 💀",
        f"{name}, ഇനി പറയുന്നത് കേട്ട് കരയരുത്! 😂",
        f"എടാ {name}, നിന്റെ future തുറന്നുനോക്കാം! 🔮",
        f"{name}, കേശവേട്ടന് എല്ലാം മനസ്സിലായി! 💀"
    ]
    return random.choice(greetings)


def get_rashi(rashi_id):
    if not rashi_id:
        return None
    for rashi in RASHIS:
        if rashi["id"] == rashi_id or rashi["name"].startswith(rashi_id):
            return rashi
    return None


def generate_prediction(name="സുഹൃത്തേ", rashi_id=None):
    name = str(name).strip() if name else "സുഹൃത്തേ"
    selected_rashi = get_rashi(rashi_id)
    movie_char = random.choice(MOVIE_CHARACTERS)
    prediction_item = random.choice(PREDICTIONS_POOL)
    dosham_item = random.choice(DOSHAMS)
    remedy = random.choice(REMEDIES)
    lucky_num = random.choice(LUCKY_NUMBERS)
    lucky_color = random.choice(LUCKY_COLORS)
    lucky_food = random.choice(LUCKY_FOODS)
    career = random.choice(BEST_CAREERS)
    quote = random.choice(KESHOO_QUOTES)

    luck_score = random.randint(1, 100)
    danger_score = random.randint(1, 100)

    return {
        "success": True,
        "name": name,
        "greeting": get_greeting(name),
        "title": f"ശ്രീ/ശ്രീമതി {name} അവരുടെ മഹാജാതകം 📜",
        "rashi": selected_rashi["name"] if selected_rashi else "നക്ഷത്രം അറിയില്ല ⭐",
        "rashi_desc": selected_rashi["desc"] if selected_rashi else "കേശവേട്ടന് പോലും അറിയില്ല! 😂",
        "prediction": prediction_item["text"],
        "tagline": prediction_item["tagline"],
        "accuracy": f"{luck_score}%",
        "dosham": dosham_item["name"],
        "dosham_desc": dosham_item["desc"],
        "remedy": remedy,
        "lucky_number": lucky_num,
        "lucky_color": lucky_color,
        "lucky_food": lucky_food,
        "best_career": career,
        "movie_character": movie_char["character"],
        "movie_movie": movie_char.get("movie", "മലയാള സിനിമ"),
        "movie_dialogue": movie_char["prediction"],
        "keshu_quote": quote,
        "character": random.choice(CHARACTER),
        "job": random.choice(JOB),
        "money": random.choice(MONEY),
        "love": random.choice(LOVE),
        "marriage": random.choice(MARRIAGE),
        "future": random.choice(FUTURE),
        "warning": random.choice(WARNING),
        "luck_score": luck_score,
        "danger_score": danger_score
    }


# =========================================================
# ROUTES
# =========================================================

@app.route("/")
def home():
    """Render the main homepage for Keshunte Pravajanam."""
    return render_template("index.html", rashis=RASHIS)


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    """Support alternative /prediction endpoint."""
    if request.method == "POST":
        data = request.form
        name = data.get("name", "സുഹൃത്തേ")
        rashi_id = data.get("rashi")
    else:
        name = request.args.get("name", "സുഹൃത്തേ")
        rashi_id = request.args.get("rashi")

    result = generate_prediction(name=name, rashi_id=rashi_id)
    return render_template("index.html", rashis=RASHIS, initial_result=result)


@app.route("/api/predict", methods=["GET", "POST"])
def api_predict():
    """API endpoint for prediction generation."""
    if request.method == "POST":
        data = request.get_json(silent=True) or request.form.to_dict() or {}
        name = data.get("name", "").strip() or "സുഹൃത്തേ"
        rashi_id = data.get("rashi") or data.get("nakshatram")
    else:
        name = request.args.get("name", "").strip() or "സുഹൃത്തേ"
        rashi_id = request.args.get("rashi") or request.args.get("nakshatram")

    result = generate_prediction(name=name, rashi_id=rashi_id)
    return jsonify(result)


@app.route("/api/porutham", methods=["GET", "POST"])
def porutham():
    """Fun Malayalam astrology compatibility matcher."""
    if request.method == "POST":
        data = request.get_json(silent=True) or request.form.to_dict() or {}
        name1 = data.get("name1", "ഒരാൾ")
        name2 = data.get("name2", "മറ്റൊരാൾ")
    else:
        name1 = request.args.get("name1", "ഒരാൾ")
        name2 = request.args.get("name2", "മറ്റൊരാൾ")

    compatibility = [
        {"percentage": "8%", "title": "പൊട്ടക്കിണർ കോംബോ! 😂", "text": f"{name1} + {name2} = ഒരുമിച്ച് project ചെയ്താൽ project തന്നെ കരയും! 💀"},
        {"percentage": "98%", "title": "റീൽസ് സോൾമേറ്റ്സ്! 📱", "text": f"{name1} reel അയക്കും. {name2} reply ചെയ്യും. പിന്നെ രണ്ടുപേരും 3 മണിക്കൂർ scroll ചെയ്യും! 😂"},
        {"percentage": "42%", "title": "കടം വാങ്ങുന്ന കൂട്ടുകെട്ട്! 💸", "text": f"{name1} ₹50 ചോദിക്കും. {name2} കൊടുക്കും. തിരിച്ചു കിട്ടില്ല! 💀"},
        {"percentage": "15%", "title": "സപ്ലി കൂട്ടുകെട്ട്! 📚", "text": f"{name1} പഠിക്കില്ല. {name2} പഠിക്കില്ല. Result രണ്ടുപേരും നോക്കും! 😂"},
        {"percentage": "100%", "title": "രണ്ടുപേരും ഒരേ ദുരന്തം! 😂", "text": f"{name1}യും {name2}യും കൂടിയാൽ ചുറ്റുമുള്ളവർക്ക് പണി! 💀"},
        {"percentage": "69%", "title": "കട്ടൻ ചായ കോംബോ! ☕", "text": f"{name1} ചായ വാങ്ങും. {name2} കുടിക്കും. Bill ആരും കൊടുക്കില്ല! 😂"},
        {"percentage": "1%", "title": "Worst Combo 💀", "text": f"{name1}യും {name2}യും ഒരുമിച്ചാൽ കേശവേട്ടൻ പോലും ഓടും! 😂"},
        {"percentage": "87%", "title": "Late Legends ⏰", "text": f"{name1} late. {name2} അതിലും late. Class തീരും! 😂"},
        {"percentage": "73%", "title": "Food Partners 🍗", "text": f"{name1} food കാണും. {name2} order ചെയ്യും. Diet പോയി! 😂"},
        {"percentage": "99%", "title": "Sleep Partners 😴", "text": f"{name1} ഉറങ്ങും. {name2} ഉറങ്ങും. Plan cancel ചെയ്യും! 😂"}
    ]
    result = random.choice(compatibility)
    return jsonify({
        "name1": name1,
        "name2": name2,
        "percentage": result["percentage"],
        "title": result["title"],
        "text": result["text"]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    is_debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=is_debug)
