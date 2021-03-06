import random

import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang="ru")


def imen(word):
    try:
        return morph.parse(word)[0].inflect({"nomn"}).word
    except:
        return word


def rod(word):
    try:
        return morph.parse(word)[0].inflect({"gent"}).word
    except:
        return word


def dat(word):
    try:
        return morph.parse(word)[0].inflect({"datv"}).word
    except:
        return word


def vin(word):
    try:
        return morph.parse(word)[0].inflect({"accs"}).word
    except:
        return word


def tvar(word):
    try:
        return morph.parse(word)[0].inflect({"ablt"}).word
    except:
        return word


def pred(word):
    try:
        return morph.parse(word)[0].inflect({"loct"}).word
    except:
        return word


def zvat(word):
    try:
        return morph.parse(word)[0].inflect({"voct"}).word
    except:
        return word


def rod2(word):
    try:
        return morph.parse(word)[0].inflect({"gen2"}).word
    except:
        return word


def vin2(word):
    try:
        return morph.parse(word)[0].inflect({"acc2"}).word
    except:
        return word


def pred2(word):
    try:
        return morph.parse(word)[0].inflect({"loc2"}).word
    except:
        return word


def get_rod(word):
    try:
        return morph.parse(word)[0].tag.gender
    except:
        return "masc"


def change_rod(word, rod_masc_femn_neut):
    try: return morph.parse(word)[0].inflect({rod_masc_femn_neut}).word
    except:
        return word


def change_time_verb(word, tense_pres_past_futr):
    try:
        morph.parse(word)[0].inflect({tense_pres_past_futr}).word
    except:
        return word


word = "технический"
