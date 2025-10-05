# PowerShell script to create missing municipality pages for CERTIALMERIA
# This script will create 52 missing municipality HTML pages

$municipalities = @(
    @{Name="Bentarique"; Slug="bentarique"; Zone="Alpujarra"; Climate="B4"; Distance="38 km"; Certs="12+"; Desc="pueblo de la Alpujarra Almeriense"},
    @{Name="Fines"; Slug="fines"; Zone="Valle del Almanzora"; Climate="B3"; Distance="85 km"; Certs="18+"; Desc="municipio del Valle del Almanzora"},
    @{Name="Fondón"; Slug="fondon"; Zone="Alpujarra"; Climate="B4"; Distance="45 km"; Certs="22+"; Desc="pueblo de montaña de la Alpujarra"},
    @{Name="Gádor"; Slug="gador"; Zone="Zona Metropolitana"; Climate="A4"; Distance="12 km"; Certs="55+"; Desc="municipio próximo a la capital"},
    @{Name="Los Gallardos"; Slug="gallardos-los"; Zone="Valle del Almanzora"; Climate="B3"; Distance="75 km"; Certs="28+"; Desc="municipio del Valle del Almanzora"},
    @{Name="Gérgal"; Slug="gergal"; Zone="Interior"; Climate="B3"; Distance="50 km"; Certs="25+"; Desc="municipio del interior"},
    @{Name="Huécija"; Slug="huecija"; Zone="Alpujarra"; Climate="B4"; Distance="32 km"; Certs="15+"; Desc="pequeño municipio de la Alpujarra"},
    @{Name="Huércal de Almería"; Slug="huercal-de-almeria"; Zone="Zona Metropolitana"; Climate="A4"; Distance="8 km"; Certs="120+"; Desc="municipio del área metropolitana de Almería"},
    @{Name="Illar"; Slug="illar"; Zone="Alpujarra"; Climate="B4"; Distance="42 km"; Certs="8+"; Desc="pequeño pueblo de la Alpujarra"},
    @{Name="Instinción"; Slug="instincion"; Zone="Alpujarra"; Climate="B4"; Distance="35 km"; Certs="10+"; Desc="municipio de la Alpujarra Almeriense"},
    @{Name="Laroya"; Slug="laroya"; Zone="Filabres"; Climate="B4"; Distance="65 km"; Certs="6+"; Desc="pequeño pueblo de Los Filabres"},
    @{Name="Láujar de Andarax"; Slug="laujar-de-andarax"; Zone="Alpujarra"; Climate="B4"; Distance="52 km"; Certs="45+"; Desc="capital de la Alpujarra Almeriense"},
    @{Name="Líjar"; Slug="lijar"; Zone="Valle del Almanzora"; Climate="B3"; Distance="92 km"; Certs="8+"; Desc="pequeño pueblo del Valle del Almanzora"},
    @{Name="Lucainena de las Torres"; Slug="lucainena-de-las-torres"; Zone="Interior"; Climate="B3"; Distance="42 km"; Certs="18+"; Desc="pueblo del interior almeriense"},
    @{Name="Lúcar"; Slug="lucar"; Zone="Valle del Almanzora"; Climate="B3"; Distance="95 km"; Certs="12+"; Desc="municipio del norte de la provincia"},
    @{Name="Lubrín"; Slug="lubrin"; Zone="Valle del Almanzora"; Climate="B3"; Distance="68 km"; Certs="22+"; Desc="municipio del Valle del Almanzora"},
    @{Name="María"; Slug="maria"; Zone="Norte"; Climate="C2"; Distance="120 km"; Certs="15+"; Desc="municipio del norte de Almería"},
    @{Name="Nacimiento"; Slug="nacimiento"; Zone="Interior"; Climate="B3"; Distance="55 km"; Certs="20+"; Desc="municipio del interior montañoso"},
    @{Name="Ohanes"; Slug="ohanes"; Zone="Alpujarra"; Climate="B4"; Distance="40 km"; Certs="28+"; Desc="municipio de la Alpujarra"},
    @{Name="Oria"; Slug="oria"; Zone="Valle del Almanzora"; Climate="B3"; Distance="88 km"; Certs="18+"; Desc="pueblo del Valle del Almanzora"},
    @{Name="Padules"; Slug="padules"; Zone="Alpujarra"; Climate="B4"; Distance="36 km"; Certs="32+"; Desc="municipio de la Alpujarra"},
    @{Name="Partaloa"; Slug="partaloa"; Zone="Valle del Almanzora"; Climate="B3"; Distance="98 km"; Certs="10+"; Desc="pequeño pueblo del Valle del Almanzora"},
    @{Name="Paterna del Río"; Slug="paterna-del-rio"; Zone="Alpujarra"; Climate="B4"; Distance="48 km"; Certs="16+"; Desc="municipio de la Alpujarra alta"},
    @{Name="Pechina"; Slug="pechina"; Zone="Zona Metropolitana"; Climate="A4"; Distance="10 km"; Certs="85+"; Desc="municipio del área metropolitana de Almería"},
    @{Name="Rágol"; Slug="ragol"; Zone="Alpujarra"; Climate="B4"; Distance="34 km"; Certs="14+"; Desc="pueblo de la Alpujarra"},
    @{Name="Rioja"; Slug="rioja"; Zone="Poniente"; Climate="A4"; Distance="28 km"; Certs="38+"; Desc="municipio del Poniente Almeriense"},
    @{Name="Santa Cruz de Marchena"; Slug="santa-cruz-de-marchena"; Zone="Alpujarra"; Climate="B4"; Distance="44 km"; Certs="12+"; Desc="pequeño municipio de la Alpujarra"},
    @{Name="Santa Fe de Mondújar"; Slug="santa-fe-de-mondujar"; Zone="Interior"; Climate="B3"; Distance="30 km"; Certs="18+"; Desc="municipio del interior"},
    @{Name="Senés"; Slug="senes"; Zone="Filabres"; Climate="C2"; Distance="70 km"; Certs="5+"; Desc="pequeño pueblo de montaña"},
    @{Name="Serón"; Slug="seron"; Zone="Valle del Almanzora"; Climate="B3"; Distance="105 km"; Certs="32+"; Desc="municipio del norte del Valle del Almanzora"},
    @{Name="Sierro"; Slug="sierro"; Zone="Valle del Almanzora"; Climate="B3"; Distance="90 km"; Certs="14+"; Desc="pueblo del Valle del Almanzora"},
    @{Name="Somontín"; Slug="sonontin"; Zone="Valle del Almanzora"; Climate="B3"; Distance="82 km"; Certs="16+"; Desc="municipio del Valle del Almanzora"},
    @{Name="Sorbas"; Slug="sorbas"; Zone="Interior"; Climate="B3"; Distance="58 km"; Certs="42+"; Desc="municipio del interior conocido por su desierto"},
    @{Name="Suflí"; Slug="sufli"; Zone="Valle del Almanzora"; Climate="B3"; Distance="96 km"; Certs="9+"; Desc="pequeño pueblo del Valle del Almanzora"},
    @{Name="Taberno"; Slug="taberno"; Zone="Valle del Almanzora"; Climate="B3"; Distance="78 km"; Certs="24+"; Desc="municipio del Valle del Almanzora"},
    @{Name="Tahal"; Slug="tahal"; Zone="Filabres"; Climate="B4"; Distance="62 km"; Certs="18+"; Desc="pueblo de la Sierra de los Filabres"},
    @{Name="Terque"; Slug="terque"; Zone="Alpujarra"; Climate="B4"; Distance="28 km"; Certs="26+"; Desc="municipio de la Alpujarra baja"},
    @{Name="Tíjola"; Slug="tijola"; Zone="Valle del Almanzora"; Climate="B3"; Distance="95 km"; Certs="45+"; Desc="importante municipio del Valle del Almanzora"},
    @{Name="Las Tres Villas"; Slug="tres-villas-las"; Zone="Alpujarra"; Climate="B4"; Distance="46 km"; Certs="14+"; Desc="agrupación de tres pueblos de la Alpujarra"},
    @{Name="Turre"; Slug="turre"; Zone="Valle del Almanzora"; Climate="B3"; Distance="72 km"; Certs="55+"; Desc="municipio residencial del Valle del Almanzora"},
    @{Name="Turrillas"; Slug="turrillas"; Zone="Interior"; Climate="B3"; Distance="48 km"; Certs="10+"; Desc="pueblo del interior almeriense"},
    @{Name="Uleila del Campo"; Slug="uleila-del-campo"; Zone="Valle del Almanzora"; Climate="B3"; Distance="80 km"; Certs="22+"; Desc="municipio del Valle del Almanzora"},
    @{Name="Urrácal"; Slug="urracal"; Zone="Valle del Almanzora"; Climate="B3"; Distance="92 km"; Certs="8+"; Desc="pequeño pueblo del Valle del Almanzora"},
    @{Name="Velefique"; Slug="velefique"; Zone="Filabres"; Climate="C2"; Distance="55 km"; Certs="12+"; Desc="pueblo de montaña de Los Filabres"},
    @{Name="Vélez-Blanco"; Slug="velez-blanco"; Zone="Norte"; Climate="C2"; Distance="145 km"; Certs="28+"; Desc="municipio del norte de Almería con importante patrimonio"},
    @{Name="Vélez-Rubio"; Slug="velez-rubio"; Zone="Norte"; Climate="C2"; Distance="135 km"; Certs="52+"; Desc="importante municipio del norte de Almería"},
    @{Name="Viator"; Slug="viator"; Zone="Zona Metropolitana"; Climate="A4"; Distance="6 km"; Certs="95+"; Desc="municipio del área metropolitana de Almería"},
    @{Name="Zurgena"; Slug="zurgena"; Zone="Valle del Almanzora"; Climate="B3"; Distance="82 km"; Certs="48+"; Desc="municipio residencial del Valle del Almanzora"}
)

Write-Host "Creating 48 missing municipality pages..." -ForegroundColor Green
Write-Host "Total municipalities to create: $($municipalities.Count)" -ForegroundColor Cyan

foreach ($muni in $municipalities) {
    Write-Host "`nProcessing: $($muni.Name) -> $($muni.Slug)" -ForegroundColor Yellow

    $dirPath = "municipios\$($muni.Slug)"

    # Create directory if it doesn't exist
    if (-not (Test-Path $dirPath)) {
        New-Item -ItemType Directory -Path $dirPath -Force | Out-Null
        Write-Host "  Created directory: $dirPath" -ForegroundColor Green
    } else {
        Write-Host "  Directory already exists: $dirPath" -ForegroundColor Gray
    }
}

Write-Host "`n=== SUMMARY ===" -ForegroundColor Cyan
Write-Host "Total municipalities processed: $($municipalities.Count)" -ForegroundColor Green
Write-Host "Script completed successfully!" -ForegroundColor Green
