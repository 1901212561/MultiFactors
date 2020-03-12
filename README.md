# MultiFactors
## 一、原始数据
### Part 1
（何老师把要下载的变量名称添加于此处）
### Part 2
（玻澜把要新增的变量名称添加于此处）
### Part 3
#### A.财务数据：

1. 过去五年：营业总收入、企业归属母公司净利润

2. 当期：企业当前市值、企业长期负债、总负债 、总资产、企业账面权益、common equity、流通股本

3. 未来三年：一致预期净利润

#### B.价量数据：

当日成交量

## 二、大类风格因子定义明细
### （一）Beta
#### A. 小类因子
1. BETA  
（1）定义  
（公式不好打可以贴图片，最好把具体方法、该怎么做解释清楚，方便后续计算）
#### B. 加权方式

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

### （八）Liquidity

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