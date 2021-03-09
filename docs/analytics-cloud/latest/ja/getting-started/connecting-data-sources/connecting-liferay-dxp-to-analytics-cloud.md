# Liferay DXPとAnalytics Cloudの接続

Liferay DXPインスタンスには、ウェブ解析データやユーザーや訪問者のデータが豊富に含まれています。 ウェブサイトの訪問者情報を監視して収集するには、データソースを追加してLiferay DXPサイトとAnalytics Cloudの接続を設定する必要があります。

繋げる方法は2つあります。

  - アクセストークンを使って接続する（推奨
  - OAuthを使って接続する

## アクセス・トークンの使用

アクセス・トークンを使用して接続するには、Liferay DXPのインストールが以下のフィックスパックの要件を満たしている必要があります。

  - 7.2 Fix Pack 5/SP2
  - 7.1 修正パック 18/SP4
  - 7.0 Fix Pack 90/SP13

要件を満たしておらず、最低限のfixpack要件にアップグレードできない場合は、代わりに[OAuth ](./connecting-liferay-dxp-using-oauth.md) を使用して接続することができます。

![DXPサイトをAnalytics Cloudに接続するには、トークンを使用するか、OAuthを使用します。](connecting-liferay-dxp-to-analytics-cloud/images/01.png)

### データソースの追加

1.  データソースを作成するには、 *Setting* \> *Data Sources* ➡> *Add Data Source*に移動します。 このアクションを実行するには、管理者ロールを持っている必要があります。

2.  データソースの種類としてLiferay DXPを選択します。 コピーするためのトークンを提供する画面が表示されます。

    ![Analytics Cloudはコピーするためのトークンを提供しています。](connecting-liferay-dxp-to-analytics-cloud/images/02.png)

3.  トークンをコピーし、Liferay DXPインスタンスに移動します。 *コントロールパネル* の下の *構成* \> *インスタンス設定* ♦> *Analytics Cloud*。 下の画像のように、Analytics Cloud TokenフィールドにAccess Tokenを貼り付け、Connectをクリックします。

    ![Liferay DXPインストールのインスタンス設定構成にAnalytics Cloudトークンを追加します。](connecting-liferay-dxp-to-analytics-cloud/images/03.png)

<!-- end list -->

``` note::
   For Liferay DXP 7.0, Analytics Cloud Admin is under *Configuration* > *Analytics Cloud*.
```

接続が成功すると、 `あなたのDXPインスタンスがAnalytics Cloudに接続されています`というメッセージが表示されます。

![成功メッセージは、DXPとAnalytics Cloud間の接続が正しく設定されていることを確認します。](connecting-liferay-dxp-to-analytics-cloud/images/04.png)

おめでとうございます。DXPがACワークスペースに接続されました。

## 次のステップ

  - [プロパティでサイトと個人を追跡する](./tracking-sites-and-individuals-using-properties.md)
  - [OAuthを使ったLiferay DXPの接続](./connecting-liferay-dxp-using-oauth.md)
