from helpers.make_request import make_request


def paginator(results, data, url, headers, num_pages):
    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        response = make_request("POST", url, headers, payload)
        data = response.json()
        results.extend(data["results"])

    return results

