from googletrans import Translator

translator = Translator()

out = translator.translate("baki sab badhiya", dest = 'en')
print(out)

dialogue = 'Are You Watching Closely?'
out = translator.translate(dialogue, dest = 'hi')
print(out.text)