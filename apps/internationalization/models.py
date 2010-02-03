from django.db import models


class DictionaryEntry(models.Model):
    text = models.CharField(null=False, max_length=100)
    meaning = models.CharField(null=False,max_length=100)
        
    class Meta:
        db_table = 'Dictionary'
    
    def __unicode__(self):
        return "%s -> %s" % (self.text, self.meaning)
    
    @staticmethod
    def load_dictionary():
        dictionary_entries = DictionaryEntry.objects.all()
        dictionary = {}
        
        for entry in dictionary_entries:
            dictionary[entry.text] = entry.meaning
        return dictionary
        
   
class Translator(models.Model):
    def __init__(self):
        self.dictionary = DictionaryEntry.load_dictionary()
    
    def translate(self, parts):
        result = ""
        for part in parts:
            result += self.dictionary[part] + " "
        return result.strip()