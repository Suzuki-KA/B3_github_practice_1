# ユーザーに名前を尋ね、挨拶メッセージを出力する関数
def hello_user():
    # ユーザーから名前を入力してもらう
    name = input("お名前を入力してください: ")

    # 挨拶メッセージを作成
    if name:
        message = f"こんにちは、{name}さん！Pythonの世界へようこそ！"
    else:
        message = "こんにちは！Pythonの世界へようこそ！"

    # メッセージを出力
    print(message)

if __name__ == "__main__":
    hello_user()