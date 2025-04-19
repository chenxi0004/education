import JSEncrypt from 'jsencrypt/bin/jsencrypt.min'
//密钥对生成http:/web.chacuo.net/netrsakeypair
const publicKey='MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKoR8mX0rGKLqzcWmOzbfj64K8ZIgOdH\n'+
'nzkXSOVOZbFu/TJhZ7rFAN+eaGkl3C4buccQd/EjEsj9ir7ijT7h96MCAwEAAQ=='
const privateKey='MIIBVAIBADANBgkqhkiG9W0BAQEFAASCAT4wggE6AgEAAkEAqhHyZfSsYourNxaY\n'+
'7Nt+PrgrxkiA50efoRdI5U51sW79MmFnusUA355oaSxcLhu5xxB38SMSyP2KvuKN\n'+
'PuH3owIDAQABAkAfoiLyL+z4lf4Myxk6xUDgLaWGximj20cuf+5BKKnlrK+Ed8gA\n'+
'kMOHqoTt2UZwA5E2MzS4EI2gjfQhz5X28uqxAiEA3WNFxfrCZlSZHb0gn2zDpWow\n'+
'cSxQAgiCstxGUoOqlW8CIQDDOerGKH5OmCJ4Z21v+F25WaHYPxCFMvwxpCw99Ecv\n'+
'DQIgIdhDTIqD2jfYjPTY8Jj3EDGPbH2HHuffvflECt3Ek60CIQCFRlCkHpi7hthh\n'+
'YhovyloRYsM+IS9h/0Bz1EAuO0ktMQIgSPT3aFAgJYWKpqRYKlLDVcflZFCKY7u3\n'+
'UP8iwi1Qw0Y='
//加密
export function encrypt(txt) {
    const encryptor = new JSEncrypt()
    encryptor.setPublicKey(publicKey) //设置公钥
    return encryptor.encrypt(txt)//对数据进行加密
}
//解密
export function decrypt(txt) {
    const encryptor = new JSEncrypt()
    encryptor.setPrivateKey(privateKey)//设置私钥
    return encryptor.decrypt(txt)//对数据进行解密
}

