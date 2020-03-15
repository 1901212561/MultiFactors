# MultiFactors
## 一、原始数据
### Part 1


| 数据名称                                     | 变量名称      |
| -------------------------------------------- | ------------- |
| **Part 1**-**基础数据**                      |               |
| 前收盘价（日）                               | close_pre     |
| 开盘价（日）                                 | open          |
| 最高价（日）                                 | high          |
| 最低价（日）                                 | low           |
| 交易量（日，手）                             | volume        |
| 交易金额（日，千元）                         | amount        |
| 交易均价（日，成交金额/成交量）              | vwap          |
| 交易状态（日）（0 停牌；1 交易；NaN 未上市） | state         |
| 所在行业（日）                               | industry      |
| **Part 2-计算风格因子所需数据**              |               |
| 总市值（日，万元）                           | mv_total      |
| 流通市值（日，万元）                         | mv_current    |
| 总股本（日，万股）                           | stock_total   |
| 流通股本（日，万股）                         | stock_current |
| 总资产（元）                                 | asset         |
| 总负债（元）                                 | liability     |
| 长期负债（元）                               | debt_long     |
| 所有者权益（元）                             | equity        |
| 普通股（股数）→股本（元）                    | stock_common  |
| 现金收益→CFO（元）                           | earning_cash  |
| 营业总收入                                   | sale          |
| 净利润                                       | ni            |
| 归母净利润                                   | ni_attr       |
| 一致预期净利润                               | ni_expect     |
| 一致预期基本EPS                              | eps_expect    |



## 二、大类风格因子定义明细
### （一）大类因子：beta   
#### 小类因子：BETA

$r_i=\alpha +\beta r_m+e_i$

过去的250天，个股收益率和沪深300指数日收益率进行半衰指数加权回归，半衰期H=60。

权重 $w_t=2^{(t-T-1)/H} (t=1,2,...,T)$

·需要的数据：个股日收益率、沪深300指数日收益率

### （二）大类因子：Momentum  
#### 小类因子 ：RSTR

$RSTR=\displaystyle \sum_{t=L}^{T+L} w_t[ln(1+r_t)]$   其中T=500，L=21

收益率序列以半衰指数加权，半衰期H=120.

$w_t=2^{(t-T-1)/H} (t=L,L+1,...,T)$

·需要的数据：个股日收益率

### （三）大类因子: Size  
#### 小类因子：LNCAP

$LNCAP=LN(total\underline\: market\underline\: capitalization)$

·需要的数据：个股总市值

### (四）大类因子：Earnings Yield

#### 4.1小类因子：EPIBS

$EPIBS=est\underline\: eps/P$

·需要的数据：$est\underline\: eps$个股一致预期基本每股收益、个股股票价格

#### 4.2小类因子：ETOP

历史EP值$ETOP=earnings\underline\:ttm/mkt\underline\:freeshares$

过去12月个股净利润/当前市值

·需要的数据：过去12个月个股净利润、个股当前市值

#### 4.3小类因子：CETOP

$CETOP=cash\underline\:earnings/P$

个股现金收益/股票价格

·需要的数据：个股现金收益、个股股票价格

### （五）大类因子：Volatility

#### 5.1小类因子：DASTD

$DASTD={(\displaystyle \sum_{t=1}^{T} w_t(r_t-\mu (r))^2)}^{1/2}$

权重 $w_t=2^{(t-T-1)/H} (t=1,2,...,T)$

收益率序列长度T=250，半衰期H=40

·需要的数据：个股收益率

#### 5.2 小类因子：CMRA

$CMRA=ln(1+max{Z(T)})-ln(1+min{Z(T)})$

其中$Z(T)=\displaystyle \sum_{\tau =1}^{T} [ln(1+r_\tau)] $      $r_\tau$为个股月收益率，T=12

·需要的数据：个股月收益率

#### 5.3小类因子：HSIGMA

$HSIGMA=std(e_i)$

$e_i$是从BETA计算中得到的


### （六）Growth

#### A. 小类因子

1. SGRO  
   过去 5 年企业营业总收入复合增长率

2. EGRO 

   过去 5 年企业归属母公司净利润复合增长率

3. EGIB

    未来 3 年企业一致预期净利润增长率

4. EGIB_S 

   未来 1 年企业一致预期净利润增长率

### （七）Value

1. BTOP

    计算企业总权益值除以当前市值。

$$
BTOP = \frac{common \ equity}{current \ market \ capitalization}
$$

### （八）Leverage

1. MLEV
   $$
   MLEV = \frac{ME+LD}{ME}
   $$
   *ME*表示企业当前市值

   *LD* 表示企业长期负债

2. DTOA

$$
DTOA = \frac{TD}{TA}
$$

 	*TD* 表示总负债 

​	 *TA* 表示总资产

3. BLEV 
   $$
   BLEV =\frac{BE+LD}{BE}
   $$
   *BE*表示企业账面权益

   *LD* 表示企业长期负债

### （九）Liquidity

1. STOM
   $$
   STOM = ln \sum_{t=1}^{21}{\frac{V_t}{S_t}}
   $$
   V_t表示当日成交量

   *S_t* 表示流通股本

2. STOQ
   $$
   STOQ = ln({\frac1{T}}\sum_{t=1}^3 e^{STOM_t})
   $$
   
3. STOA
   $$
   STOQ = ln({\frac1{T}}\sum_{t=1}^{12} e^{STOM_t})
   $$

#### 注：加权方式

我们利用样本内单类因子回归最小化残差平方和的方法得到小类因子的组合权重
