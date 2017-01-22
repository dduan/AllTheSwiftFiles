import urllib2
import json
import sys

'''
This script collects name, clone url and star counts for top swift repos from Github.

It takes two arguments:
    - Github access token
    - # of stars required for repos to be included
'''

def collect_repos_with_stars_more_than(token, star_count):
    done = False
    page = 0
    results = []
    names = set()
    while not done:
        url = 'https://api.github.com/search/repositories?access_token={}&q=language:Swift&sort=stars&page={}'.format(token, page)
        response = json.loads(urllib2.urlopen(url).read())
        repos = [{
            'clone_url': item['clone_url'],
            'stars': item['stargazers_count'],
            'name': item['full_name']
            } for item in response['items'] if not item['full_name'] in names]
        names.update([r['name'] for r in repos])
        results += [repo for repo in repos if repo['stars'] > star_count]
        if len(repos):
            done = repos[-1]['stars'] < star_count
        page += 1
    return results

if __name__ == '__main__':
    repos = collect_repos_with_stars_more_than(sys.argv[1], int(sys.argv[2]))
    print(json.dumps(repos, indent=4))
