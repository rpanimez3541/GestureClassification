from flickrapi import FlickrAPI
import pandas as pd
import sys
key='f5d1291b86942c7cbd6a73a1da78df33'
secret='1b8752f26a45bdbd'
def get_urls(MAX_COUNT, image_tag):
    flickr = FlickrAPI(key, secret)
    photos = flickr.walk(text=image_tag,
                            tag_mode='all',
                            tags=image_tag,
                            extras='url_o',
                            per_page=50,
                            sort='relevance')
    count=0
    urls=[]
    for photo in photos:
        if count< MAX_COUNT:
            count=count+1
            print("Fetching url for image number {}".format(count))
            try:
                url=photo.get('url_o')
                urls.append(url)
            except:
                print("Url for image number {} could not be fetched".format(count))
        else:
            print("Done fetching urls, fetched {} urls out of {}".format(len(urls),MAX_COUNT))
            break
    urls=pd.Series(urls)
    print("Writing out the urls in the current directory")
    urls.to_csv(image_tag+"_urls.csv")
    print("Done!!!")
def main():
    MAX_COUNT=int(sys.argv[1])
    sep=","
    tag1=sys.argv[2]
    tag2=sys.argv[3]
    tag3=sys.argv[4]
    seq=(tag1, tag2, tag3)
    tags=sep.join(seq)
    get_urls(MAX_COUNT, tags)
if __name__=='__main__':
    main()