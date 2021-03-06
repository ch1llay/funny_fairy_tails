import random

import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang="ru")


def imen(word):
    w = morph.parse(word)[0].inflect({"nomn"}).word
    if not w:w = word
    return w


def rod(word):
    w = morph.parse(word)[0].inflect({"gent"}).word
    if not w:w = word
    return w


def dat(word):
    w = morph.parse(word)[0].inflect({"datv"}).word
    if not w:w = word
    return w


def vin(word):
    w = morph.parse(word)[0].inflect({"accs"}).word
    if not w:w = word
    return w


def tvar(word):
    w = morph.parse(word)[0].inflect({"ablt"}).word
    if not w:w = word
    return w


def pred(word):
    w = morph.parse(word)[0].inflect({"loct"}).word
    if not w:w = word
    return w


def zvat(word):
    w = morph.parse(word)[0].inflect({"voct"}).word
    if not w:w = word
    return w


def rod2(word):
    w = morph.parse(word)[0].inflect({"gen2"}).word
    if not w:w = word
    return w


def vin2(word):
    w = morph.parse(word)[0].inflect({"acc2"}).word
    if not w: w = word
    return w


def pred2(word):
    w = morph.parse(word)[0].inflect({"loc2"}).word
    if not w: w = word
    return w


def get_rod(word):
    w = morph.parse(word)[0].tag.gender
    if not w: w = "masc"
    return w


def change_rod(word, rod_masc_femn_neut, temse_pres_past_ftur=None):
    w = morph.parse(word)[0].inflect({rod_masc_femn_neut}).word
    if not w:w = word
    return w


def change_time_verb(word, tense_pres_past_futr, rod):
    w = morph.parse(word)[0].inflect({tense_pres_past_futr, rod}).word
    if not w: w = word
    return w

# word = morph.parse("ложка")[0].inflect({"accs"}).word
# print(word)

