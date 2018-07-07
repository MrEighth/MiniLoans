# UncleClub

## 1.项目架构

TODO：业务逻辑图

![业务逻辑图](https://images2015.cnblogs.com/blog/811883/201704/811883-20170423150019101-1710764799.jpg)

## 2.项目结构

| 路径                 | 描述 |
| :------------------ | -----------  |
| /README.md          | 项目描述      |
| /requirements.txt   | 依赖及版本说明 |
| /config.py          | Flask配置类   |
| /manage.py          | 工程启动文件   |
| /migrations         | 数据迁移      |
| /tests              | 单元测试模块   |
| /venv               | 虚拟环境      |
| /conf               | 全局配置文件   |
| /lib                | 依赖模块      |
| /logs               | 网站日志      |
| /webapps            | 网络应用层    |
| /webapps/controllers| 业务逻辑层    |
| /webapps/models     | 数据模型层    |
| /webapps/scripts    | 底层         |
| /webapps/templates  | 模板         |
| /webapps/routes     | 路由表        |
| /webapps/static     | 资源文件      |

## 3.网站简明设计

TODO：补全设计

### 1.account管理

#### 1.1 客户(L1)

申请、联系客服

#### 1.2 客服(L2)

审批（同意、拒绝（反馈））- 过滤掉本人账户

#### 1.3 经理(L3)

放款、催款 - 过滤掉本人账户

#### 1.4 admin(L4)

配置权限（提高权限、删除权限）



### 2.flow管理 — Views

common css

#### 2.0 引流 + 小程序

利率介绍、公司介绍。。。

func：联系客服（微信二维码，备注：申请）

#### 2.1 注册

account：微信、手机号、QQ

info：身份证、芝麻信用。。。

func：联系客服（微信二维码，备注：申请）

#### 2.2 申请权限

面试成为客服、经理

func：联系客服（微信二维码，备注：申请）

#### 2.3 个人(负)资产

infos(余额、下次还款金额、还款时间、还款方式说明、平台信用度 default 0)

func：联系客服（微信二维码，备注：申请）

#### 2.4 GM-申请-客服

data But审批

#### 2.5 GM-放款、还款-经理

#### 2.6 admin

#### 2.7 数据可视化 - eCharts

流量监控、毛利统计(扣除成本：短信服务、OCR云服务)。。。

### 3.数据库管理

TODO：。。。