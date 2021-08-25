from django.shortcuts import render
from main.models import *
# Create your views here.

def homepage(request):
    return render(request, template_name='main/home.html')

def teamspage(request):
    teams = Teams.objects.all()
    return render(request, template_name='main/teams.html',context={'teams':teams})

def lioneerspage(request):
    df_lioneers = scrap('https://zh.wikipedia.org/zh-tw/%E6%96%B0%E7%AB%B9%E8%A1%97%E5%8F%A3%E6%94%BB%E5%9F%8E%E7%8D%85')
    df_players = scrap2('https://pleagueofficial.com/stat-player/2020-21')
    alldata = pd.merge(df_lioneers,df_players, on='姓名',how='left').fillna(0).to_dict('records')
    return render(request, template_name='main/lioneers.html',context={'alldata':alldata})

def dreamerspage(request):
    df_dreamers = scrap('https://zh.wikipedia.org/zh-tw/%E7%A6%8F%E7%88%BE%E6%91%A9%E6%B2%99%E5%8F%B0%E6%96%B0%E5%A4%A2%E6%83%B3%E5%AE%B6')
    df_players = scrap2('https://pleagueofficial.com/stat-player/2020-21')
    alldata = pd.merge(df_dreamers,df_players, on='姓名',how='left').fillna(0).to_dict('records')
    return render(request, template_name='main/dreamers.html',context={'alldata':alldata})

def pilotspage(request):
    df_pilots = scrap('https://zh.wikipedia.org/zh-tw/%E6%A1%83%E5%9C%92%E9%A0%98%E8%88%AA%E7%8C%BF')
    df_pilots['姓名'][0] = '喬登'
    df_players = scrap2('https://pleagueofficial.com/stat-player/2020-21')
    alldata = pd.merge(df_pilots,df_players, on='姓名',how='left').fillna(0).to_dict('records')
    return render(request, template_name='main/pilots.html',context={'alldata':alldata})

def bravespage(request):
    df_braves = scrap('https://zh.wikipedia.org/zh-tw/%E8%87%BA%E5%8C%97%E5%AF%8C%E9%82%A6%E5%8B%87%E5%A3%AB')
    df_players = scrap2('https://pleagueofficial.com/stat-player/2020-21')
    alldata = pd.merge(df_braves,df_players, on='姓名',how='left').fillna(0).to_dict('records')
    return render(request, template_name='main/braves.html',context={'alldata':alldata})