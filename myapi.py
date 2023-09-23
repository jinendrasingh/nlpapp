import paralleldots


class API:
    def __init__(self):
        paralleldots.set_api_key("hzhll1czoCdPqfLN9ZQ3NZEoxh8DxUD6M8Hpv8OGI8E")

    def sentiment_analysis(self, text):
        lang_code = "en"
        response = paralleldots.sentiment(text, lang_code)
        return response

    def ner_analysis(self, text):
        lang_code = "en"
        response = paralleldots.ner(text, lang_code)
        return response

    def emotion_analysis(self, text):
        response = paralleldots.emotion(text)
        return response
