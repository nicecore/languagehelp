langs_list = []

language_data = """
Pashto - پښتو
Uzbek - Oʻzbek
Turkmen - Türkmen
Swedish - svenska
Albanian - Shqip
Arabic - العربية
English - 
Samoan - gagana fa'a Samoa
Catalan - català
Portuguese - Português
Russian - Русский
Spanish - Español
Guaraní - Avañe'ẽ
Armenian - Հայերեն
Dutch - Nederlands
(Eastern) Punjabi - ਪੰਜਾਬੀ
German - Deutsch
Azerbaijani - azərbaycan dili
Bengali - বাংলা
Belarusian - беларуская мова
French - français
Dzongkha - རྫོང་ཁ
Aymara - aymar aru
Quechua - Runa Simi
Bosnian - bosanski jezik
Croatian - hrvatski jezik
Serbian - српски језик
Tswana - Setswana
Norwegian - Norsk
Norwegian Bokmål - Norsk bokmål
Norwegian Nynorsk - Norsk nynorsk
Malay - bahasa Melayu
Bulgarian - български език
Fula - Fulfulde
Kirundi - Ikirundi
Khmer - ខ្មែរ
Sango - yângâ tî sängö
Chinese - 中文 (Zhōngwén)
Lingala - Lingála
Kongo - Kikongo
Swahili - Kiswahili
Luba-Katanga - Tshiluba
Cook Islands Māori - Māori
Greek - ελληνικά
Turkish - Türkçe
Czech - čeština
Slovak - slovenčina
Danish - dansk
Fang - Fang
Tigrinya - ትግርኛ
Tigre - ትግረ
Kunama - Kunama
Saho - Saho
Bilen - ብሊና
Nara - Nara
Afar - Afar
Estonian - eesti
Amharic - አማርኛ
Faroese - føroyskt
Fijian - vosa Vakaviti
Fiji Hindi - फ़िजी बात
Rotuman - Fäeag Rotuma
Finnish - suomi
Georgian - ქართული
Greenlandic - kalaallisut
Chamorro - Chamoru
Haitian - Kreyòl ayisyen
Latin - latine
Italian - Italiano
Hungarian - magyar
Icelandic - Íslenska
Hindi - हिन्दी
Indonesian - Bahasa Indonesia
Persian (Farsi) - فارسی
Kurdish - Kurdî
Irish - Gaeilge
Manx - Gaelg
Hebrew - עברית
Japanese - 日本語 (にほんご)
Kazakh - қазақ тілі
Kyrgyz - Кыргызча
Lao - ພາສາລາວ
Latvian - latviešu valoda
Southern Sotho - Sesotho
Lithuanian - lietuvių kalba
Luxembourgish - Lëtzebuergesch
Macedonian - македонски јазик
Malagasy - fiteny malagasy
Chichewa - chiCheŵa
Malaysian - بهاس مليسيا
Divehi - ދިވެހި
Maltese - Malti
Marshallese - Kajin M̧ajeļ
Romanian - Română
Mongolian - Монгол хэл
Burmese - ဗမာစာ
Afrikaans - Afrikaans
Nauruan - Dorerin Naoero
Nepali - नेपाली
Māori - te reo Māori
Korean - 한국어
Urdu - اردو
Polish - język polski
Kinyarwanda - Ikinyarwanda
Tamil - தமிழ்
Slovene - slovenski jezik
Somali - Soomaaliga
Southern Ndebele - isiNdebele
Swati - SiSwati
Tsonga - Xitsonga
Venda - Tshivenḓa
Xhosa - isiXhosa
Zulu - isiZulu
Sinhalese - සිංහල
Romansh - N/A
Tajik - тоҷикӣ
Thai - ไทย
Tonga (Tonga Islands) - faka Tonga
Ukrainian - Українська
Bislama - Bislama
Vietnamese - Tiếng Việt
Shona - chiShona
Northern Ndebele - isiNdebele
"""


language_lines = language_data.strip().split('\n')

for line in language_lines:
    english_name, native_name = line.split(' - ')
    langs_list.append(english_name.strip())
    langs_list.append(native_name.strip())

langs_list_str = ",".join(langs_list)
