#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import requests
import json
import time
import random


tokenBotTelegram = '787110238:AAFqLDrocbbOnSbKp8iWmthCEJwKfnw3M2Y'
id_grupo='-1001250058237'
url = 'https://api.chucknorris.io/jokes/random'
tb = telebot.TeleBot(tokenBotTelegram)

def contarLineasArchivo(archivo):
    
    lineas = open(archivo, 'r')  
    contadorDeLineas = 0

    for linea in lineas.readlines():
        contadorDeLineas = contadorDeLineas + 1

    lineas.close()
    return contadorDeLineas


def frasesMasBellasDelMundo(archivo):
    
    lasFrasesMasBellasDelMundo = open(archivo, 'r', encoding='utf-8')
    fraseAleatoria = (random.randint(1,contarLineasArchivo(archivo)))
    contador = 0

    for frase in lasFrasesMasBellasDelMundo.readlines():
    
        contador = contador + 1
        
        if contador == fraseAleatoria:
            f_string = str(frase)
            
    
    lasFrasesMasBellasDelMundo.close()
    return f_string.replace('\n','')


def chuck():
    
    response = requests.get(url)

    if response.status_code == 200:
        contenido = json.loads(response.content)
        joke_about_chuck = contenido['value']
    
    return joke_about_chuck


def manualDelChico():
    opciones = """

        /frases: Te dirá algunas de sus frases mas bellas del mundo, para dedicarla a alguna peuca.
        /chuck: Experimental para probar API Rest.
        /tiempo: El tiempo de hoy.
        /temblor: En construcción.

    """
    return opciones

def tiempoHoy():

    url = 'http://api.meteored.cl/index.php?api_lang=cl&localidad=18578&affiliate_id=4y6u4lm6bjpi&v=3.0'
    response = requests.get(url)
    contenido = json.loads(response.content)

    daysDict = contenido['day']
    todayResponse = daysDict.get('1')

    min = todayResponse.get('tempmin')
    max = todayResponse.get('tempmax')

    r = """
    Aqui les voy a dar el tiempo a los muy aweonaos
    Temperatura mínima : {tempMin} °C
    Temperatura máxima : {tempMax} °C
    """.format(tempMin = min, tempMax = max)

    return r

def main():

    @tb.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        tb.reply_to(message, manualDelChico())


    @tb.message_handler(commands=['frases'])
    def send_message(message):
        tb.reply_to(message, frasesMasBellasDelMundo('frases.txt'))


    @tb.message_handler(commands=['chuck'])
    def send_message(message):
        tb.reply_to(message, chuck())

    @tb.message_handler(commands=['tiempo'])
    def send_message(message):
        tb.reply_to(message, tiempoHoy())
    
    
    tb.polling()

if __name__ == "__main__":
    main()