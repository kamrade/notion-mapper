import requests
from yaspin import yaspin


# only POST for now !!!
def make_request(method, url, headers, payload):

    with yaspin(text="Loading data", color="green") as spinner:
        try:
            if method == "POST":
                response = requests.post(url, json=payload, headers=headers)
            else:
                print("Unsupported method")
        except requests.exceptions.RequestException as e:
            spinner.text = ""
            spinner.fail(f"🔴 Request {url} error")
            raise SystemExit(e)
        else:
            if response:
                if response.status_code != 200:
                    spinner.text = ""
                    spinner.fail(f"🔴 Request {url} status {response.status_code}")
                    print("Connection error with Notion API")
                    raise SystemExit()

                spinner.text = ""
                spinner.ok(f"✅ Request {url} success")
                return response

            else:
                spinner.text = ""
                spinner.fail(f"🔴 Request {url} failed")
                raise SystemExit()

