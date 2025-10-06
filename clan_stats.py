import sys
import os
import csv
import requests
from dotenv import load_dotenv

def check_clan(clan, limit, save_csv):

    obj = []
    token = os.getenv('CR_API_TOKEN')
    response = requests.get(
        f"https://proxy.royaleapi.dev/v1/clans/%23{clan.replace('#', '')}/riverracelog?limit={limit}",
        headers={"Authorization": "Bearer {}".format(token)},
    )

    print(f"https://proxy.royaleapi.dev/v1/clans/%23{clan.replace('#', '')}/riverracelog?limit={limit}")
    trophies = 0
    if response.status_code == 200:
        data = response.json()['items']
        for entry in data:
            for standing in entry['standings']:
                rr_clan = standing['clan']

                if rr_clan['tag'] == clan:
                    week = f"{entry['seasonId']}-{entry['sectionIndex'] + 1}"
                    trophies = rr_clan['clanScore']
                    sum = 0
                    decks = 0
                    print(f"-- week: {week} --")
                    print(f"clan: {rr_clan['name']} ({standing['rank']}. place)")
                    print(f"cw trophies: {trophies}")
                    for player in rr_clan['participants']:
                        sum += player['fame']
                        decks += player['decksUsed']
                    print(f'sum: {sum}, decks: {decks}')
                    if sum != 0:
                        print(f'avg: {round(sum/decks, 2)}')
                    print()
                    obj.append({"week": week, "trophies": trophies, "decksUsed": decks, "score": sum})
    else:
        print(f"Error: {response.status_code}")

    if not save_csv:
        return
    if not os.path.exists('clan_stats'):
         os.makedirs('clan_stats')

    filename = 'clan_stats/clan_{}.csv'.format(clan.replace('#', ''))
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile: 
        writer = csv.DictWriter(csvfile, ['week', 'trophies', 'decksUsed', 'score'], delimiter=';')
        writer.writeheader()
        writer.writerows(obj) 

    csvfile.close()

    print(f"Data has been written to {filename}")

if __name__ == "__main__":
    load_dotenv()

    argc = len(sys.argv)
    if argc > 1:
        clan_tag = sys.argv[1]
        
        limit = 10
        if argc > 2:
            limit = int(sys.argv[2]) or 10

        if argc > 3 and sys.argv[3] == "-csv":
            check_clan(clan_tag, limit, save_csv=True)
        else:
            check_clan(clan_tag, limit, save_csv=False)
    else:
        print('usage: `clan_stats.py "<clan tag>" <number of weeks>`')
        exit()
