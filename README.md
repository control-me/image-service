# image-service

## Access the service

Set the `path` query parameter in the url to a path from the default storage bucket at `gs://controlme-dev.appspot.com`.

```
https://controlme-dev.appspot.com/images/serving-url?path=/web-app/waz311v.png
```

## Deployment

In order to get access to Google's high performance image serving infrastructure, I have created a small app engine project that allows for a single HTTP request to retrieve a serving URL for any blob within your Google Cloud project. Start by deploying the service to your project:

```bash
gcloud app deploy
```

Your production URL is at `gcloud-project.appspot.com` according to your project ID.

### Endpoints

_Request_  
`GET /images/serving-url?path=/web-app/image.png`  
Generate a serving URL for an image in the default storage bucket.

_Response_

```
200 OK
[Content-Type="text/plain"]
"https://lhx.ggpht.com/randomStringImageId"
```

<hr />

_Request_  
`GET /images/serving-url/redirect?path=/web-app/image.png`  
Redirect to the serving URL for an image in the default storage bucket.

_Response_

```
302 Found
[Location="https://lhx.ggpht.com/randomStringImageId"]
""
```

### Errors

```
400 Bad Request
[Content-Type="application/json"]
{ error: "error-id", message: "Error message" }
```

## Serving URL format

#### Format

```javascript
params = [`${key}${v===true?'':v}`, ...];
image = `${url}=${params.join("-")}`;
```

Example to make an avatar image:

```
https://lhx.ggpht.com/randomStringImageId=s72-cc
```

<details>
<summary><b>Parameters</b></summary>
<p>

```
int:  s   ==> Size
int:  w   ==> Width
bool: c   ==> Crop
hex:  c   ==> BorderColor
bool: d   ==> Download
int:  h   ==> Height
bool: s   ==> Stretch
bool: h   ==> Html
bool: p   ==> SmartCrop
bool: pa  ==> PreserveAspectRatio
bool: pd  ==> Pad
bool: pp  ==> SmartCropNoClip
bool: pf  ==> SmartCropUseFace
int:  p   ==> FocalPlane
bool: n   ==> CenterCrop
int:  r   ==> Rotate
bool: r   ==> SkipRefererCheck
bool: fh  ==> HorizontalFlip
bool: fv  ==> VerticalFlip
bool: cc  ==> CircleCrop
bool: ci  ==> ImageCrop
bool: o   ==> Overlay
str:  o   ==> EncodedObjectId
str:  j   ==> EncodedFrameId
int:  x   ==> TileX
int:  y   ==> TileY
int:  z   ==> TileZoom
bool: g   ==> TileGeneration
bool: fg  ==> ForceTileGeneration
bool: ft  ==> ForceTransformation
int:  e   ==> ExpirationTime
str:  f   ==> ImageFilter
bool: k   ==> KillAnimation
int:  k   ==> FocusBlur
bool: u   ==> Unfiltered
bool: ut  ==> UnfilteredWithTransforms
bool: i   ==> IncludeMetadata
bool: ip  ==> IncludePublicMetadata
bool: a   ==> EsPortraitApprovedOnly
int:  a   ==> SelectFrameint
int:  m   ==> VideoFormat
int:  vb  ==> VideoBegin
int:  vl  ==> VideoLength
bool: lf  ==> LooseFaceCrop
bool: mv  ==> MatchVersion
bool: id  ==> ImageDigest
int:  ic  ==> InternalClient
bool: b   ==> BypassTakedown
int:  b   ==> BorderSize
str:  t   ==> Token
str:  nt0 ==> VersionedToken
bool: rw  ==> RequestWebp
bool: rwu ==> RequestWebpUnlessMaybeTransparent
bool: rwa ==> RequestAnimatedWebp
bool: nw  ==> NoWebp
bool: rh  ==> RequestH264
bool: nc  ==> NoCorrectExifOrientation
bool: nd  ==> NoDefaultImage
bool: no  ==> NoOverlay
str:  q   ==> QueryString
bool: ns  ==> NoSilhouette
int:  l   ==> QualityLevel
int:  v   ==> QualityBucket
bool: nu  ==> NoUpscale
bool: rj  ==> RequestJpeg
bool: rp  ==> RequestPng
bool: rg  ==> RequestGif
bool: pg  ==> TilePyramidAsProto
bool: mo  ==> Monogram
bool: al  ==> Autoloop
int:  iv  ==> ImageVersion
int:  pi  ==> PitchDegrees
int:  ya  ==> YawDegrees
int:  ro  ==> RollDegrees
int:  fo  ==> FovDegrees
bool: df  ==> DetectFaces
str:  mm  ==> VideoMultiFormat
bool: sg  ==> StripGoogleData
bool: gd  ==> PreserveGoogleData
bool: fm  ==> ForceMonogram
int:  ba  ==> Badge
int:  br  ==> BorderRadius
hex:  bc  ==> BackgroundColor
hex:  pc  ==> PadColor
hex:  sc  ==> SubstitutionColor
bool: dv  ==> DownloadVideo
bool: md  ==> MonogramDogfood
int:  cp  ==> ColorProfile
bool: sm  ==> StripMetadata
int:  cv  ==> FaceCropVersion
```

</p>
</details>
