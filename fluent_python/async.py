import string
import random


def generate_urls(base_url, num_urls):
    for _ in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))
    
if __name__ == "__main__":
    urls = generate_urls("http://foo.com/", 10)
    import ipdb; ipdb.set_trace()
    
    