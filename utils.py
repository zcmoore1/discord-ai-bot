from youtubesearchpython import VideosSearch

def get_youtube_url(search_term: str, n: int):
    # Search for the query
    videos_search = VideosSearch(search_term, limit=n)
    
    # Get results
    results = videos_search.result()['result']
    
    if results:
        # Extract video URL
        res = [r['link'] for r in results]
        return res
    else:
        return None