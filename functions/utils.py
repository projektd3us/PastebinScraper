from os.path import exists
from functions.googlr import search
import requests as req
import os
import glob


def keyListSearch(keyList, numOfRes, sincePub):  # takes a keywordList, number of res. and time since added
    """
    Search on google for a keyword from keyList, by a number of results, and a date of results.

    :param list keyList: list of keywords to search
    :param int numOfRes: num of results to return
    :param str sincePub: h(hour), d(day), m(month) or a(all)

    :rtype: list
    :return: List of results
    """

    # add type checks?
    results = []
    if sincePub == 'a':
        since = ''
    else:
        since = str('qdr:' + sincePub)

    # main searcher
    for key in keyList:
        pastebinKey = 'site:pastebin.com ' + key
        for url in search(pastebinKey, tbs=since, stop=numOfRes):
            if '/u/' not in url:  # balcklist user pastebins
                results.append(url)  # current search results

    return results


def downAndRetLoc(url):  # download to location temp and return location of download
    """
    Download a file by url (to temp folder) and return its path. Works for urls without file extensions, turns them into rawUrls.

    :param str url: url in form of string

    :rtype: str
    :return: path of downloaded file
    """
    pasteCode = url.rsplit('/', 1)[1]  # pastebin code
    filename = pasteCode + ".txt"  # filename given by pastebin code
    rawURL = url.rsplit('/', 1)[0] + "/raw/" + pasteCode  # getting the raw url
    request = req.get(rawURL, allow_redirects=True)  # setup req api
    path = "files\\temp\\" + filename  # compute path
    with open(path, 'wb') as f:
        if not exists(path):  # check if download unnecessary
            f.write(request.content)  # download req
        return path


def cleanPath(abs_path):  # cleans a folder
    """
    Removes all files from a folder at the given path.

    :param str abs_path: absolute path of folder in form of string
    """
    files = glob.glob(abs_path)  # list of files in path to be cleaned
    for f in files:
        os.remove(f)  # remove file


def fileToLineList(path):  # todo replace with direct iteration of file lines if possible
    """
    Takes a file and creates list from its lines.

    :param str path: file path in form of string

    :rtype: list
    :return: list of file lines
    """
    return open(path).readlines()  # list from file lines


def simpleSearchDown(keyword):
    """
    Simple search and download function, downloading the first 10 found results

    :param str keyword: a keyword to be searched on google
    """
    urllist = (keyListSearch([keyword], 10, 'a'))
    for i in urllist:
        print(downAndRetLoc(i))
