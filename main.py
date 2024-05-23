


# If you want to work through a proxy, specify the proxy in the format: TYPE://LOGIN:PASSWORD@IP:PORT
# 10 FREE proxies: https://www.webshare.io/?referral_code=fp27vdieqruw

proxy = 'http://bnlrgm:7qx41ojpiu@8.46.169.83:5074'


def parsing(keywords):
    from modules.parser import Parser

    parser = Parser('your_email', 'your_password', proxy=None, headless=True)

    for key in keywords:
        # parser.login()

        parser.parse_by_keyword(key)


def downloading(keywords):
    from modules.downloader import Downloader

    for key in keywords:
        downloader = Downloader(key, proxy=None, headless=True)
        links = downloader.read_links_file()

        for index, link in enumerate(links, 1):
            print(f"Processing link {index}/{len(links)}")
            downloader.download(link)



if __name__ == '__main__':
    keys = [
        'keto',
    ]

    choice = input("Enter '1' to run the parser, '2' to run the downloader: ")

    if choice == '1':
        parsing(keys)
    elif choice == '2':
        downloading(keys)
    else:
        print("Invalid choice. Please enter '1' or '2'.")

