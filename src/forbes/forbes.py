# -*- coding: utf-8 -*-
import json


def get_forbes_json():
    """Return forbes json."""
    with open('./forbes.json') as data_file:
        forbes_json = json.load(data_file)
    return forbes_json


def create_billionaire_dictionary(forbes_json):
    """Return dict with age as key, values are name, net worth and industry."""
    bill_dict = {}
    for idx in range(len(forbes_json)):
        key = forbes_json[idx]['name']
        value = (forbes_json[idx]['age'], forbes_json[idx]['net_worth (USD)'], forbes_json[idx]['source'])
        bill_dict[key] = value
    return bill_dict


def create_filtered_billionaire_list(bill_dict):
    """Return list of tuples with billionaires under 80 and over 0 years."""
    filtered_list = []
    for key in bill_dict:
        if bill_dict[key][0] > 0 and bill_dict[key][0] < 80:
            filtered_list.append((key, bill_dict[key][0], bill_dict[key][1], bill_dict[key][2]))
    return filtered_list


def scrooge_mcduck_and_richie_rich(filtered_list):
    """Return oldest/youngest billionaire under 80, by name, net worth, industry."""
    scrooge = filtered_list[0][1]
    richie = filtered_list[0][1]
    for idx in range(len(filtered_list)):
        if filtered_list[idx][1] > scrooge:
            oldest = filtered_list[idx]
            scrooge = filtered_list[idx][1]
        if filtered_list[idx][1] < richie:
            youngest = filtered_list[idx]
            richie = filtered_list[idx][1]
    oldest = (oldest[0], oldest[2], oldest[3])
    youngest = (youngest[0], youngest[2], youngest[3])
    return oldest, youngest
