# データソースの接続

環境やデータ・ソースが誤って設定されていると、Liferay DXPのデータ・ソースへのアクセスを妨げたり、中断させたりすることがあります。 ここでは、DXP データソースの問題をトラブルシューティングする方法をご紹介します。

## アナリティクスクラウドへのネットワークアクセスがない

次のURLを許可リストに追加して、DXPのインストールで弊社のAnalytics Cloudサーバーへのインターネットアクセスが可能であることを確認してください。

  - `https://analytics.liferay.com`
  - `https://osbasahpublisher-{weDeployKey}.lfr.cloud`
  - `https://osbasahbackend-{weDeployKey}.lfr.cloud`
  - `https://analytics-js-cdn.liferay.com`

<!-- end list -->

``` note::
   Please contact Liferay Analytics Cloud Support at help.liferay.com to obtain your ``{weDeployKey}`` value.
```

``` important::
   企業のイントラネットの利用状況を分析するなど、いくつかのユースケースでは、訪問者のブラウザもファイアウォールの背後にあります。 このシナリオでは、企業のオフィスネットワークが上記のURLのアウトバウンドアクセスも許可していることを確認する必要があります。
```

## アナリティクスクラウドへの接続を検証する

データがAnalytics Cloudに送信されているかどうかを検証するのに役立つヒントをご紹介します。

### アナリティクスのイベント

アナリティクスのイベントは、クライアントのブラウザから直接送信されます。 データがAnalytics Cloudに送信されていることを確認するには、次の手順を実行します。

1.  追跡されているDXPウェブサイトのページをご覧ください。

2.  ブラウザのインスペクタを開き、「ネットワーク」タブに移動します。

3.  ネットワーク タブを XHR でフィルタリングします。

4.  ページを更新してください。

5.  `osbasahpublisher`から始まるリクエストが出ていることを確認します。 リクエストは以下のスクリーンショットのようなものになります。

    ![Analytics Cloudへの接続を検証します。](connecting-data-sources/images/01.png)

    この要求が表示されている場合は、お客様のウェブサイトがアナリティクス データをアナリティクス クラウド ワークスペースに送信していることを意味します。 リクエストペイロードをチェックして、 `channelId`という変数があることを確認してください。 `channelID` がnullの場合、データソースは現在OAuth接続を使用しています。 `channelId` が数字の文字列の場合は、現在トークン接続を使用しています。

### 連絡先データ

DXPは、ログインユーザーの連絡先情報を個別のプロファイルデータとしてAnalytics Cloudに送信します。 このデータはDXPサーバーから直接送信されます。

連絡先データが送信されていることを確認するには、DXPサーバーのログに以下のようなメッセージがないか確認してください。

    INFO  [liferay/analytics_messages_processor-1][AddAnalyticsMessagesMessageListener:70] Added 500 analytics messages
    
    INFO  [liferay/analytics_messages_processor-1][AddAnalyticsMessagesMessageListener:70] Added 500 analytics messages
    
    INFO  [liferay/scheduler_dispatch-3][SendAnalyticsMessagesMessageListener:149] Sent 100 analytics messages
    
    INFO  [liferay/scheduler_dispatch-3][SendAnalyticsMessagesMessageListener:164] Deleted 100 analytics messages

これらのサーバーログが表示されている場合は、連絡先データが正常にACに送信されていることを示しています。

## データ処理時間

データが Analytics Cloud に到着すると、ワークスペース ダッシュボードに表示される前に、処理にさらに時間がかかります。

アナリティクス イベントの場合は、サイト ダッシュボードの 24 時間フィルターの訪問者メトリクスを 10 分から 15 分以内に表示できるようにする必要があります。

![アナリティクス データが一定期間で入ってくる。](connecting-data-sources/images/02.png)

セッション期間やバウンス率などの他のセッション関連データは、訪問者のセッションが終了するまで待つ必要があります。 ビジターセッションは、30分間の非活動時間が経過した時点、またはUTC 00:00:00:00のいずれか早い時点で終了したとみなされます。

個人のプロフィールは、処理に時間がかかり、時間の経過とともに利用可能になります。

## 認証の再試行

**Error Message:** `Unknown error. 認証を再試行してください。`

DXPデータソースへのアクセスには、DXPインスタンスが公開されていること、およびAnalytics Cloudインスタンスが[OAuthアプリケーションとしてDXPインスタンスに登録されていることが必要です](../getting-started/connecting-data-sources/connecting-liferay-dxp-using-oauth.md)。

**解決策：**

1.  [Liferay DXPデータ・ソースの追加](../getting-started/connecting-data-sources/connecting-liferay-dxp-using-oauth.md)の手順に従ってください。

2.  [Analytics Cloud を DXP インスタンスに登録する](../getting-started/connecting-data-sources/connecting-liferay-dxp-using-oauth.md#registering-analytics-cloud-with-your-liferay-dxp-instance).

## サポートされていないバージョン

**Error Message:** `Unsupported version. この接続方法は、データソースのLiferayバージョンをサポートしていません。 Liferay 7.0/7.1インスタンスに接続していることを確認するか、別の接続方法を試してみてください。`

**解決策：**

1.  connect with a Liferay DXP 7.0 or 7.1 instance]を確認してください。

2.  [Liferay DXPデータ・ソースの追加](../getting-started/connecting-data-sources/connecting-liferay-dxp-using-oauth.md)の手順に従ってください。

3.  エラーが続く場合は、DXPインスタンスでJSONウェブサービスが有効になっていることを確認してください。 デフォルトで有効になっています。 [ポータルプロパティ](https://docs.liferay.com/dxp/portal/7.1-latest/propertiesdoc/portal.properties.html#JSON) の設定 json.web.service.enabled=false (例えば、 [portal-ext.properties ファイル](https://learn.liferay.com/dxp/7.x/en/installation-and-upgrades/reference/portal-properties.html)に設定) を使用して無効にした場合は、設定を削除するか、プロパティの値を true に設定してください。

## 無効な資格情報、認証の期限切れ

**Error Message:** `Invalid Credentials. このデータ ソースの認証は失効しました。 OAuthタブでトークンを再認証してください。`

このメッセージはログに表示されます。

    WARN [http-nio-8080-exec-14][AbstractOAuthService:88] Unsecure HTTP, Transport Layer Security is recommended

DXP データソースへの接続は、DXP インスタンスのウェブサーバープロトコルを転送する必要があります。

**解決策：**

1.  DXP データ ソースを追加する手順に従って、特に [に注意して Analytics Cloud を DXP インスタンス](../getting-started/connecting-data-sources/connecting-liferay-dxp-using-oauth.md#registering-analytics-cloud-with-your-liferay-dxp-instance)に登録します。

2.  問題が解決せず、Web サーバー プロトコルが転送される場合は、DXP インスタンスの [portal-ext.properties](https://learn.liferay.com/dxp/7.x/en/installation-and-upgrades/reference/portal-properties.html) ファイルにこれらの [ポータル プロパティ](https://docs.liferay.com/dxp/portal/7.1-latest/propertiesdoc/portal.properties.html) を設定してください。

<!-- end list -->

    web.server.forwarded.protocol.enabled=true
    redirect.url.security.mode=domain
    redirect.url.domains.allowed=
