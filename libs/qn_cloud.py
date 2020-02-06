from qiniu import Auth, put_file, etag

from swiper import conf
def upload_to_qiniu(filename,filepath):

    # 构建鉴权对象
    q = Auth(conf.QN_ACCESSKEY, conf.QN_SECRETKEY)
    # 上传后保存的文件名
    key = filename
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(conf.QN_BUCKET, key, 3600)
    # 要上传文件的本地路径
    localfile = filepath
    put_file(token, key, localfile)
    url='%s%s'%(conf.QN_BASE_URL,filename)
    return url
