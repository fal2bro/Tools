import matplotlib.pyplot as plt
from wordcloud import WordCloud
import MeCab
import re

def CreateWordcloud(text):

    # MeCabを使用して日本語の単語を抽出

    #mecab = MeCab.Tagger("-Owakati")
    #text_wakati = mecab.parse(text)

    #意味をなさない単語を除外する
    filtered_text = filter_words(text)

    ##フォントの選択
    #font_path="Wordcloud\Fonts\ipaexg.ttf"
    #font_path="Wordcloud\Fonts\DotGothic16-Regular.ttf"
    font_path=r"Wordcloud\Fonts\BIZUDGothic-Bold.ttf"


    # WordCloudオブジェクトを作成
    max_words = 100 #単語の最大値
    min_font_size=2 #フォントサイズの最小値

    #colormapは適宜修正，matplotlibのカラーマップ
    wordcloud = WordCloud(width=400, height=400, background_color='white', colormap='winter', collocations=False, font_path=font_path,max_words=max_words,min_font_size=min_font_size).generate(filtered_text)

    # 画像を描画するためのプロットを作成
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # 画像を表示
    plt.show()



def filter_words(text):
    mecab = MeCab.Tagger()
    node = mecab.parseToNode(text)
    words = []
    
    # ストップワードリスト, 適宜修正すること
    stop_words = {'思い','さい','せ','よう','い','さ','う','よ','の', 'が', 'は', 'に', 'を', 'と', 'も', 'で', 'から', 'や', 'ば', 'へ', 'けど', 'です', 'ます', 'この', 'その', 'あの', 'だ', 'いる', 'ある', 'する', 'こと'}
    
    while node:
        word = node.surface
        pos = node.feature.split(',')[0]
        #ひらがなを除外
        if re.match(r'^[\u3040-\u309F]+$', word):
            node = node.next
            continue
        # 助詞、助動詞、記号、接続詞、ストップワードを除外
        if pos not in ['助詞', '助動詞', '記号', '接続詞'] and word not in stop_words:
            words.append(word)
        node = node.next
    
    return ' '.join(words)


if __name__ == '__main__':
    filename = input("ファイルパスを指定してください: ") #txtファイル
    with open(filename, 'r', encoding='shift_jis') as file:
        mytext = file.read()
    CreateWordcloud(mytext)
