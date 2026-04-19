# Design System — Foundation Tokens

> 基于美团外卖视觉规范 `01-Foundation.md`，颜色命名参照 Material Design 3 语义逻辑。

---

## 1. Color

### 1.1 Reference Tokens（原始色值层）

> 直接来自规范，不做推断扩展。组件不直接引用此层。

```
ref.color.brand.default       #00B85C
ref.color.red.default         #FF1F1F
ref.color.orange.default      #FF7700
ref.color.blue.default        #166FF7
ref.color.purple.default      #882EFF
ref.color.pink.default        #EB2F93
ref.color.brown.default       #9E7549

ref.color.neutral.10          #111925
ref.color.neutral.20          #343B45
ref.color.neutral.40          #646971
ref.color.neutral.60          #94979D
ref.color.neutral.80          #B7BABD
ref.color.neutral.90          #CFD1D3

ref.color.surface.scrim       #000000 @ 50%
ref.color.outline.default     #DCDDDF
ref.color.outline.variant     #E7E8E9
ref.color.background.page     #F3F3F4
ref.color.background.card     #F8F8F8
```

---

### 1.2 Color Ramps（色阶）

> 基于规范原值 HSL 插值推导，stop 400 = 规范原值。

#### Brand Green

| Stop | Hex | 用途 |
|------|-----|------|
| 50 | `#E6F9EF` | 浅色背景、Tag 背景、成功状态底色 |
| 100 | `#B3EDCE` | — |
| 200 | `#80E0AD` | — |
| 300 | `#40CA84` | — |
| **400** | **`#00B85C`** | **规范原值 · 按钮、导航、Tab、主操作** |
| 500 | `#009649` | 按钮 Hover 态 |
| 600 | `#007538` | 按钮 Pressed 态 · Tag 文字色 |
| 700 | `#005428` | — |
| 800 | `#003418` | 深色文字（用于浅色背景上） |
| 900 | `#00180B` | — |

#### Error Red

| Stop | Hex | 用途 |
|------|-----|------|
| 50 | `#FFF0F0` | 错误背景、Tag 背景 |
| 100 | `#FFD0D0` | — |
| 200 | `#FFA8A8` | — |
| 300 | `#FF7070` | — |
| **400** | **`#FF1F1F`** | **规范原值 · 警示按钮、错误状态、上升数据** |
| 500 | `#D41010` | 按钮 Hover 态 · 错误文字色 |
| 600 | `#A80000` | 按钮 Pressed 态 · Tag 文字色 |
| 700 | `#7A0000` | — |
| 800 | `#500000` | — |
| 900 | `#280000` | — |

---

### 1.3 System Tokens（语义角色层）

> 组件直接引用此层，不直接用 ref 或色阶 hex。

#### Primary（品牌主色）

```
sys.color.primary             #00B85C   ← brand.green.400
sys.color.primary.hover       #009649   ← brand.green.500
sys.color.primary.pressed     #007538   ← brand.green.600
sys.color.on-primary          #FFFFFF
```

#### Error（错误 / 警示）

```
sys.color.error               #FF1F1F   ← error.red.400
sys.color.error.hover         #D41010   ← error.red.500
sys.color.error.pressed       #A80000   ← error.red.600
sys.color.on-error            #FFFFFF
sys.color.error.text          #D41010   ← error.red.500，用于错误提示文字
sys.color.error.container     #FFF0F0   ← error.red.50，用于错误背景
sys.color.on-error-container  #A80000   ← error.red.600，容器内文字
```

#### Warning（提醒）

```
sys.color.warning             #FF7700
sys.color.on-warning          #FFFFFF
```

#### Success（成功，复用 primary）

```
sys.color.success             #00B85C   ← 与 primary 共用
sys.color.success.container   #E6F9EF   ← brand.green.50
sys.color.on-success-container #007538  ← brand.green.600
sys.color.on-success          #FFFFFF
```

#### Business Tags（业务标签专属色）

```
sys.color.tag.purple          #882EFF
sys.color.tag.blue            #166FF7
sys.color.tag.pink            #EB2F93
sys.color.tag.brown           #9E7549
sys.color.tag.orange          #FF7700
sys.color.tag.green           #00B85C
sys.color.tag.red             #FF1F1F
```

#### Surface（表面层次）

```
sys.color.background          #F3F3F4   ← 页面背景（最底层）
sys.color.surface             #FFFFFF   ← 卡片 / 组件默认表面
sys.color.surface-variant     #F8F8F8   ← 卡片内嵌套背景
sys.color.on-surface          #111925   ← surface 上主文字
sys.color.on-surface-variant  #343B45   ← surface-variant 上文字
```

#### Outline（描边与分割）

```
sys.color.outline             #DCDDDF   ← 按钮、文本框等线性描边
sys.color.outline-variant     #E7E8E9   ← 页面分割线
```

#### Scrim（遮罩）

```
sys.color.scrim               #000000 @ 50%   ← 弹窗遮罩
```

---

### 1.4 Text Color Tokens

```
sys.color.text.primary        #111925   ← 一级：页面标题、按钮文字
sys.color.text.secondary      #343B45   ← 二级：正文
sys.color.text.tertiary       #646971   ← 三级：辅助、说明
sys.color.text.quaternary     #94979D   ← 四级：次辅助
sys.color.text.placeholder    #B7BABD   ← 五级：输入 placeholder
sys.color.text.disabled       #CFD1D3   ← 六级：禁用态文字
sys.color.background.disabled #F3F3F4  ← 禁用态容器背景，复用页面背景色
```

---

## 2. Typography

### 2.1 Font Family

```
sys.typescale.font-family     "PingFang SC", -apple-system, sans-serif
```

### 2.2 Type Scale

| Token | Size | Line Height | 用途 |
|---|---|---|---|
| `sys.typescale.display-lg` | 48px | 68px | 重要数字、强调信息 |
| `sys.typescale.display-md` | 44px | 62px | 重要数字、强调信息 |
| `sys.typescale.display-sm` | 40px | 56px | 重要数字、强调信息 |
| `sys.typescale.headline-lg` | 36px | 50px | 模块标题、详情页正文 |
| `sys.typescale.headline-md` | 32px | 44px | 模块标题、详情页正文 |
| `sys.typescale.body-lg` | 28px | 40px | 正文、次要信息 |
| `sys.typescale.body-md` | 24px | 34px | 辅助、说明信息 |
| `sys.typescale.body-sm` | 20px | 28px | 弱说明，慎用 |

---

## 3. Spacing（Grid）

> 基准单位 4px。

### Small（组内间距）

| Token | Value | 用途 |
|---|---|---|
| `sys.spacing.xs` | 4px | 最紧凑内间距 |
| `sys.spacing.sm` | 8px | — |
| `sys.spacing.md` | 12px | — |
| `sys.spacing.lg` | 16px | — |
| `sys.spacing.xl` | 20px | — |

适用：卡片内容间距、按钮 / 标签内间距

### Medium（组件间距）

| Token | Value | 用途 |
|---|---|---|
| `sys.spacing.2xl` | 24px | — |
| `sys.spacing.3xl` | 28px | — |
| `sys.spacing.4xl` | 32px | — |
| `sys.spacing.5xl` | 36px | — |

适用：卡片间、可操作标签间

### Large（模块间距）

| Token | Value | 用途 |
|---|---|---|
| `sys.spacing.6xl` | 48px | — |
| `sys.spacing.7xl` | 60px | — |

适用：模块间大分隔、标题在模块外的距离

---

## 4. Shape（Border Radius）

| Token | Value | 用途 |
|---|---|---|
| `sys.shape.corner.full` | 20px | 最大通栏卡片、半屏弹窗 |
| `sys.shape.corner.xl` | 16px | 模态弹窗、图片 |
| `sys.shape.corner.lg` | 12px | 卡片、矩形按钮、文本框、数字输入框、图片（≥100px）、Toast、气泡 |
| `sys.shape.corner.md` | 8px | 小型组件：分段控件、复选框、图片（<100px） |
| `sys.shape.corner.sm` | 4px | 静态标签、图片（<100px）最小圆角 |

---

## 5. Elevation（Shadow）

> 格式：`color / offset-x offset-y / blur`

### High（高层级）

```
sys.elevation.high
  color:  #000000 @ 16%
  offset: 0px 12px
  blur:   36px
```

适用：悬浮标签栏、气泡、卡片容器

### Medium（中层级）

```
sys.elevation.medium
  color:  #000000 @ 10%
  offset: 0px 6px
  blur:   12px
```

适用：悬浮按钮、滑块、卡片容器

### Low（低层级）

```
sys.elevation.low
  color:  #000000 @ 4%
  offset: 0px 2px
  blur:   4px
```

适用：分段器、开关

---

## 附：Token 命名层级说明

| 前缀 | 含义 | 使用方 |
|---|---|---|
| `ref.*` | Reference — 原始值 | 不直接用于组件 |
| `sys.*` | System — 语义角色 | 组件直接引用 |
| `comp.*` | Component — 组件级（待扩展） | 单个组件内部 |

---

*待扩展：Dark mode sys token 映射 / Component tokens（Button、Input、Nav 等）*
