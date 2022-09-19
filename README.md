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

## CRUD query

### Fund
#### Create
```
mutation createMutation {
  createFund(fundData: {comptrollerProxy: "test", vaultProxy: "test", denominatedAsset: "test", creator: "test", name: "test"}) {
    fund {
      comptrollerProxy
      vaultProxy
      denominatedAsset
      creator
      name
    }
  }
}
```
#### Read
##### Funds
```
query {
  allFunds {
		name
    creator
    denominatedAsset
    vaultProxy
    comptrollerProxy
  }
}
```
##### Fund
```
query {
  fund (comptrollerProxy:"test"){
		name
    creator
    denominatedAsset
    vaultProxy
    comptrollerProxy
  }
}
```
#### Update
```
mutation updateMutation {
  updateFund(fundData: {comptrollerProxy: "test", vaultProxy: "test2", denominatedAsset: "test2", creator: "test2", name: "test2"}) {
    fund {
      comptrollerProxy
      vaultProxy
      denominatedAsset
      creator
      name
    }
  }
}
```
#### Delete
```
mutation deleteMutation{
  deleteFund(comptrollerProxy: "test") {
    fund {
      comptrollerProxy
    } 
  }
}
```

## Run scripts
```
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

## Note
### when
#### 重啟
##### Before
- export:Liquidity managements
##### After
- import:Liquidity managements

#### ReDeploy
```
poetry export --without-hashes --format=requirements.txt > requirements.txt
// git add, commit & push
```