from chirpy.core.regex.util import OPTIONAL_TEXT_PRE
from chirpy.core.regex.regex_template import RegexTemplate

SEXUAL_UNIGRAM = {'anal',
 'anus',
 'asshole',
 'bdsm',
 'blowjobs',
 'blowjob',
 'bondage',
 'boobies',
 'boobs',
 'booty',
 'butthole',
 'butts',
 'clitoris',
 'cock',
 'deepthroat',
 'dick',
 'dicks',
 'dildo',
 'dildos',
 'fellatio',
 'fuck',
 'fucking',
 'horny',
 'humping',
 'intercourse',
 'masturbate',
 'masturbated',
 'masturbating',
 'masturbation',
 'naked',
 'nipples',
 'nude',
 'orgasm',
 'penis',
 'penises',
 'porn',
 'pornhub',
 'porno',
 'pornography',
 'pornos',
 'prostitution',
 'pussies',
 'pussy',
 'sex',
 'sexy',
 'sperm',
 'testicles',
 'tities',
 'vagina',
 'vaginas'}

SEXUAL_BIGRAM = {'a penis',
 'a pussy',
 'about sex',
 'add sex',
 'anal sex',
 'big boobs',
 'big dick',
 'big tities',
 'blow me',
 'butt cheek',
 'butt cheeks',
 'butt holes',
 'butt nugget',
 'butt plug',
 'butt sex',
 'double penetration',
 'eating butt',
 'eating pussy',
 'fuck face',
 'fuck me',
 'gay porn',
 'gay sex',
 'have sex',
 'having sex',
 "he's sexy",
 'her boobs',
 'her breasts',
 'his butt',
 'his dick',
 'his penis',
 'i masturbated',
 "i'm horny",
 "i'm naked",
 "it's butthole",
 'jack off',
 'jerk off',
 'jerking off',
 'my anus',
 'my balls',
 'my booty',
 'my butt',
 'my dick',
 'my penis',
 'my pussy',
 'naked girls',
 'naked women',
 'oral sex',
 'play porn',
 'poopy butt',
 'porn movies',
 'porn stars',
 'porno movies',
 'pussy cat',
 'sex pistols',
 'sex toys',
 'sexual intercourse',
 'sexual positions',
 'sexy girls',
 'sexy lady',
 'strip clubs',
 'suck dick',
 'sucking dick',
 'the butt',
 'the penis',
 'the sex',
 'the sexy',
 'the vagina',
 'this dick',
 'this vagina',
 'watch porn',
 'watching porn',
 'your ass',
 'your asshole',
 'your butt',
 'your butthole',
 'your dick',
 'your pussy',
 'your vagina'}

SEXUAL_TRIGRAM = {'a big butt',
 'a porn star',
 'alexa lick butt',
 'being a bitch',
 'big booty bitches',
 'fuck you fuck',
 'fucking my girlfriend',
 'girls gone wild',
 'he want sex',
 'i had sex',
 'i have hiv',
 'i like boobies',
 'i like masturbating',
 'i like penis',
 'i like penises',
 'i like porn',
 'i like sex',
 'i love penises',
 'i love sex',
 "i'm very horny",
 "let's have sex",
 "my wife's pussy",
 'poopy butt hole',
 'pornhub dot com',
 'puss in boots',
 'see more butts',
 'sex with you',
 'suck a dick',
 'suck my balls',
 'suck my dick',
 'talk about sex',
 'the strip club',
 'up your ass',
 'what is sex',
 'x rated movies',
 "you're a whore",
 "your mom's ass",
 "your mom's butt",
 "your mom's pussy"}


class SexualOffensesTemplate(RegexTemplate):
    slots = {
        'sexual': list(SEXUAL_UNIGRAM | SEXUAL_BIGRAM | SEXUAL_TRIGRAM)
    }
    templates = [
        OPTIONAL_TEXT_PRE + "{sexual}", # match any utterance ending with these words
    ]
    positive_examples = [
        ('can you give me a blowjob', {'sexual': 'blowjob'}),
        ('i want to talk about sex', {'sexual': 'talk about sex'}),
        ('i love fucking my girlfriend', {'sexual': 'fucking my girlfriend'})
    ]
    negative_examples = [
        'i want to talk about sex education',
        'life is so much easier when we have sex daily', 
    ]

INAPPROP_UNIGRAMS = {'anal',
 'barf',
 'blood',
 'boogers',
 'butthole',
 'cocaine',
 'crack',
 'crap',
 'fart',
 'farts',
 'hell',
 'hentai',
 'heroin',
 'hitler',
 'lolita',
 'marijuana',
 'nazis',
 "nigger's",
 'poo',
 'poop',
 'rape',
 'retard',
 'sissy',
 'torture',
 'turds',
 'weed',
 'xxx',
 'nigger',
 'niggar'}

INAPPROP_BIGRAMS = {'a fart',
 'adolf hitler',
 'alexa fart',
 'butt face',
 'butt holes',
 'butt nugget',
 'chicken butt',
 'eating butt',
 'fart face',
 'fart head',
 'go fart',
 'his butt',
 'his dick',
 'i poop',
 "i'm stupid",
 "it's poop",
 'monkey butt',
 'mr. poop',
 'my ass',
 'my balls',
 'my butt',
 'my butthole',
 'my poop',
 'nazi germany',
 'not shit',
 'poo poo',
 'poop fart',
 'poop head',
 'poop poop',
 'poopy butt',
 'poopy poop',
 "she's sexy",
 'shits creek',
 'smoke weed',
 'smoking weed',
 'strip club',
 'strip clubs',
 'stupid people',
 'the fart',
 'the poop',
 'world domination',
 'your butthole',
 'your poop'}

INAPPROP_TRIGRAMS = {'are you drunk',
 'are you ugly',
 'backdoor sluts 9',
 'big booty bitches',
 'can you fart',
 'can you poop',
 'did you fart',
 'do you fart',
 'do you poop',
 'i have hiv',
 'i like farts',
 'i like poop',
 'i smoked weed',
 'naked mole rat',
 'poo poo head',
 'poo poo pants',
 'poopy butt hole',
 'smoke some weed',
 'talk about farts',
 'talk about poop',
 'the strip club',
 'your ugly face'}

class InappropOffensesTemplate(RegexTemplate):
    slots = {
        'inapprop': list(INAPPROP_UNIGRAMS | INAPPROP_BIGRAMS | INAPPROP_TRIGRAMS)
    }
    templates = [
        OPTIONAL_TEXT_PRE + "{inapprop}", # match any utterance ending with these words
    ]
    positive_examples = [
        ('can we talk about poop', {'inapprop': 'talk about poop'}),
        ("let us feast on my poop", {'inapprop': 'my poop'}),
        ('i am going to hell', {'inapprop': 'hell'})
    ]
    negative_examples = [
        'i want to talk about sex education',
        "i want to talk about hell\'s kitchen",
        "i want to learn more about hitler's demise"
    ]