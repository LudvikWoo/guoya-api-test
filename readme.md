# 一、版本发布
## 1. 本地打包
```
python setup.py sdist  
```
## 2. 发布版本
```
pip install twine
twine upload dist/gy-api-tool-1.0.0.tar.gz
```