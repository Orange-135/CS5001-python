import re

class UserInfo:
    def __init__(self, user_data):
        data_list = user_data.split(",")
        self.email = data_list[3]
        self.language = data_list[-1]

    def __repr__(self):
        return f"({self.email}, {self.language})"


class DataAnalysis:
    def __init__(self, file):
        # TODO: set up the necessary instance variables
        self.email = {}
        self.language = {}
        self.read_data(file)

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        try:
            with open(file_name, "r") as f:
                next(f)  # skip header line
                for line in f:
                    line = line.strip()
                    user = UserInfo(line)
                    domain = re.findall(r'\.([a-z]{2})\Z', user.email)
                    if len(domain) == 1:
                        key = domain[0]
                        self.email[key] = self.email.get(key, 0) + 1
                    self.language[user.language] = self.language.get(user.language, 0) + 1
        except FileNotFoundError:
            print(f"Can't find {file_name}")

    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.
    def top_n_lang_freqs(self, num):
        language_by_count = sorted(
            self.language.items(),
            key=lambda x: x[1], 
            reverse=True)
        total = sum(self.language.values())
        return [(lang, count / total) for lang, count in language_by_count[:num]]
    
    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered 
    # from highest frequency to lowest.

    def top_n_country_tlds_freqs(self, num):
        country_by_count = sorted(
            self.email.items(), 
            key=lambda x: x[1],
            reverse=True)
        total = sum(self.email.values())
        return [(country, count / total) for country, count in country_by_count[:num]]
    
    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.