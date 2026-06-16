import streamlit as st

st.title("ラッキーファッション診断アプリ")
st.caption("星座とラッキーナンバーから、あなたを輝かせる今日のスタイルを見つけましょう。")

st.markdown("---")
st.subheader("ラッキーファッション診断")
st.write(" 星座や好きな数字を選ぶと、今日のラッキーファッションと着こなしのアドバイスを表示するアプリを作成する。")

# --- ここから演習のコード ---

# 1. ユーザー入力（星座と数字）
sign = st.selectbox(
    "あなたの星座を選んでください",
    ["牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"]
)

lucky_number = st.selectbox(
    "ラッキーナンバーを選んでください",
    list(range(1, 11)) # 1から10まで
)

# 2. ファッション診断データの定義 (2025年トレンドを反映)
fashion_data = {
    "牡羊座": {"item": "パワーレッドのジャケット", "advice": "情熱的な赤が自信を引き出します。メタルアクセを添えて。", "image": "red.jpg"},
    "牡牛座": {"item": "クワイエット・ラグジュアリーなジレ", "advice": "上質な素材感にこだわって。アースカラーが運気を安定させます。", "image": "be-ju.jpg"},
    "双子座": {"item": "ミックスプリントのシャツ", "advice": "遊び心のある柄の組み合わせが吉。軽やかなレイヤードを楽しんで。", "image": "tshirt.jpg"},
    "蟹座": {"item": "ホワイトのワンピース", "advice": "優しい色合いがあなたの魅力を引き立てます。パールの小物と好相性。", "image": "white.jpg"},
    "獅子座": {"item": "メタルアクセサリー", "advice": "シンプルな服装に主役でアクセサリーを", "image": "metaru.jpg"},
    "乙女座": {"item": "ミッキーTシャツ", "advice": "来てるだけでディズニー気分。", "image": "miccky.jpg"},
    "天秤座": {"item": "ボヘミアン・リバイバルのブラウス", "advice": "芸術的なフリルや刺繍を取り入れて。バランスの良い配色を意識しましょう。", "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=500"},
    "蠍座": {"item": "ゴシック調のパワーコルセット", "advice": "ミステリアスな黒と深い紫を基調に。エッジの効いた小物が鍵となります。", "image": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=500"},
    "射手座": {"item": "アスレジャースタイルのスニーカー", "advice": "動きやすさと高級感を両立させて。アクティブな一日が約束されます。", "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500"},
    "山羊座": {"item": "伝統的なヘリンボーンのブレザー", "advice": "クラシックな仕立てがプロフェッショナルな印象に。足元はローファーで。", "image": "jaketto.jpg"},
    "水瓶座": {"item": "サイバーパンク風のテックアウター", "advice": "未来的な素材やデザインに挑戦して。シルバーの小物が運気を底上げ。", "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500"},
    "魚座": {"item": "マーメイドコアなスリップドレス", "advice": "幻想的なスタイルが吉。", "image": "doresu.jpg"}
}

# 3. 診断ボタン実行
if st.button("今日のスタイルを診断する！"):
    result = fashion_data[sign]
    
    st.markdown("---")
    st.subheader(f"✨ {sign}のあなたの診断結果")
    
    st.write(f"今日のラッキーアイテムは... **【 {result['item']} 】**")
    st.write(f"👗 **スタイル・アドバイス**: {result['advice']}")
    st.write(f"✨ さらに、今日は **{lucky_number}個** のアクセサリーを身につけると完璧です！")
    
    # 画像表示
    st.image(result['image'], caption=f"Recommended Style: {result['item']}", use_container_width=True)

# --- ここまで演習のコード ---

st.markdown("---")
st.info("💡 自分の好きなファッション画像を 'images/' フォルダに入れてパスを指定することも可能です。")
