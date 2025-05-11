import google.generativeai as genai
import os

try:
    # --- 1. APIキーの設定 ---
    # 環境変数からAPIキーを読み込む (推奨)
    api_key = 'AIzaSyDMktDwkpg08lbJvKfLx2gNKZDoEtK8KsQ'


    # --- 2. モデルの選択と初期化 ---
    # 利用可能なモデルを確認することもできます:
    # for m in genai.list_models():
    #   if 'generateContent' in m.supported_generation_methods:
    #     print(m.name)

    # 一般的なテキスト生成には 'gemini-pro' を使用
    model = genai.GenerativeModel('gemini-pro')

    # --- 3. プロンプトの準備 ---
    prompt = "Pythonで簡単なWebサーバーを立てる方法を教えてください。"

    # --- 4. コンテンツ生成のリクエスト ---
    print(f"--- プロンプトを送信中 ---")
    print(f'"{prompt}"')
    response = model.generate_content(prompt)

    # --- 5. レスポンスの表示 ---
    print("\n--- Geminiからの応答 ---")
    # response.text で生成されたテキストを取得できます
    print(response.text)

    # --- (オプション) レスポンスの詳細情報を確認 ---
    # print("\n--- レスポンス詳細 ---")
    # print(response) # レスポンスオブジェクト全体
    # print(response.prompt_feedback) # プロンプトに関するフィードバック (セーフティ評価など)
    # print(response.candidates) # 複数の候補がある場合など

except ValueError as ve:
    print(f"設定エラー: {ve}")
except Exception as e:
    print(f"コンテンツの生成中にエラーが発生しました: {e}")
    print("APIキーが正しいか、ネットワーク接続を確認してください。")