## QuickStart
```
poetry 

```

## 資料夾結構
```
├── core/ -> django 設定程式(.py)
├── fund/ -> django fund app 程式(.py)
│   ├── asset_weight -> 權重計算
├── web3
│   ├── contracts -> Enzyme 合約(.sol)
│   └── web3_py -> 使用和約的程式碼(web3.py)
├── deployment/ -> 合約 ABI,以及各種 ABI (.json)
```

## Developement
```
# run 
// local db
export DJANGO_SETTINGS_MODULE=core.settings_dev
// product db
export DJANGO_SETTINGS_MODULE=core.settings

python manage.py runserver

# run Django Q cluster
python manage.py qcluster

# run scripts
./manage.py shell < management/tasks.py
```

## Deployment
use railway
1. setup environment variables
2. setup build and deploy command
3. run `railway up`

how to run django_q and web server in same app
```
railway run python manage.py qcluster
```
than kills the teminal, it will run in the same app




## 手動測試部分(有時候調用合約掛掉,可以手動測)
```
# batch approve
./manage.py shell < management/tasks/multicall_approve.py

# batch liquidity management
./manage.py shell < management/tasks/liquidity_management_pangolin.py

# batch price feed update
./manage.py shell < management/tasks/multicall_price_feed.py         

```

## Note
### when
#### 重啟
