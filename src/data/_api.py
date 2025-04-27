import requests

def search_info(palavra):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{palavra}"
    response = requests.get(url)

    if response.status_code != 200:
        return

    data = response.json()[0]

    word_data = {
        "phonetic": "",
        "audio": "",
        "definition": "",
        "target_word": palavra,
        "setence": ""
    }

    # Phonetics
    ipa = ""
    audio = ""
    if data.get("phonetics"):
        for item in data["phonetics"]:
            if item.get("text"):
                ipa = item["text"]
                word_data["phonetic"] = ipa
            if item.get("audio"):
                audio = item["audio"]
                word_data["audio"] = audio
                break

    # Meanings
    meanings = data.get("meanings", [])
    if not meanings:
        return

    definition = meanings[0]["definitions"][0].get("definition", "")
    word_data["definition"] = definition
  
    return word_data

def google_translate(api_key, texto, origem="en", destino="pt"):
    url = "https://translation.googleapis.com/language/translate/v2"

    params = {
        'q': texto,
        'source': origem,
        'target': destino,
        'format': 'text',
        'key': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        resultado = response.json()
        return resultado['data']['translations'][0]['translatedText']
    else:
        print("Erro:", response.text)
        return None