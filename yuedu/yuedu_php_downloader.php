<?php
/**
* Author: 52pojie - @smldhz
* Update: 2020-2-4 16:12
* LastTime: 2020-02-05 19:53
* downSite: https://yd.51zhy.cn/
* usage: php yuedu_php_downloader.php <bid>
*/
define('DETAIL_API','https://bridge.51zhy.cn/transfer/Content/Detail?');
define('AUTHORIZE_API','https://bridge.51zhy.cn/transfer/content/authorize');
define('DEVICE_KEY','3uKpxtFAoOeqQQ0S');
 
if ($argc !==2) {
        echo "php ".__FILE__." id\n";
        die();
}
$book_id = $argv[1];
$parms = array (
        'AccessToken' => 'null',
        'DeviceToken' => 'ebookF32BE444AF96C3BB0E71BF02D648DD9C',
        'ApiName' => '/Content/Detail',
        'BridgePlatformName' => 'phei_yd_web',
        'random' => '0.'.mt_rand(),
        'AppId' => '3',
        'id' => $book_id,
);
 
$details_json = do_request(DETAIL_API.http_build_query($parms));
$details = json_decode($details_json, true);
if ($details['Code']!='200') {
        die('请求出错!-1');
}
$token = $details['Data']['ExtendData']['AuthorizeToken'];
$book_name = $details['Data']['Title'];
$file_name = "《".$book_name."》.pdf";
echo "开始下载:《".$book_name."》.pdf\n";
$parms = array (
        'IsOnline' => 'true',
        'AccessToken' => 'null',
        'DeviceToken' => 'ebookF32BE444AF96C3BB0E71BF02D648DD9C',
        'ApiName' => 'content/authorize',
        'BridgePlatformName' => 'phei_yd_web',
        'random' => '0.'.mt_rand(),
        'AppId' => '3',
        'id' => $book_id,
        'authorizeToken' => $token,
);
$authorize_json = do_request(AUTHORIZE_API, true, http_build_query($parms));
$authorize = json_decode($authorize_json, true);
if ($authorize['Code']!='200') {
        die('请求出错!-2');
}
$book_key = $authorize['Data']['Key'];
$book_url = $authorize['Data']['Url'];
$book_aes_key = get_book_aes_key($book_key);
$book = do_download($book_url);
$decrypted_book = decrypt_book($book,$book_aes_key);
file_put_contents($file_name, $decrypted_book);
echo "\n下载完成!\n";
function do_download($url){
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($ch, CURLOPT_NOPROGRESS, false);
        curl_setopt($ch, CURLOPT_PROGRESSFUNCTION, 'download_callback');
        $ret = curl_exec($ch);
        return $ret;
}
 
function download_callback($resource, $downloadSize = 0, $downloaded = 0, $uploadSize = 0, $uploaded = 0){
        echo "下载中: $downloaded/$downloadSize\r";
}
 
function get_book_aes_key($book_key){
        return openssl_decrypt(base64_decode($book_key), "AES-128-ECB", DEVICE_KEY,OPENSSL_RAW_DATA);
}
function decrypt_book($book,$key){
        return openssl_decrypt($book, "AES-128-ECB", $key,OPENSSL_RAW_DATA);
}
 
function do_request($url,$is_post = false,$post_data = ''){
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        if ($is_post) {
                curl_setopt($ch, CURLOPT_POST, 1);
                curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
        }
        $ret = curl_exec($ch);
        return $ret;
}