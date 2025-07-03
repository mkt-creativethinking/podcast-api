#!/usr/bin/env python3
"""
API simplificada para teste com n8n
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Adicionar diretório do projeto ao path
sys.path.append(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app, origins="*", allow_headers=["Content-Type", "Authorization"])

@app.route('/n8n/health', methods=['GET'])
def health_check():
    """Health check para n8n"""
    return jsonify({
        "status": "healthy",
        "service": "podcast-automation",
        "version": "1.0.0",
        "timestamp": "2025-07-01T09:00:00Z"
    })

@app.route('/n8n/status', methods=['GET'])
def system_status():
    """Status detalhado do sistema"""
    return jsonify({
        "success": True,
        "data": {
            "system_status": "online",
            "api_info": {
                "version": "1.0.0",
                "environment": "development"
            },
            "components": {
                "gossip_scraper": "operational",
                "script_generator": "operational",
                "audio_generator": "operational",
                "cover_generator": "operational",
                "video_generator": "operational"
            }
        }
    })

@app.route('/n8n/gossips/search', methods=['POST'])
def search_gossips():
    """Buscar fofocas para n8n"""
    data = request.get_json() or {}
    limit = data.get('limit', 5)
    min_score = data.get('min_score', 6.0)
    
    # Simular busca de fofocas
    fake_gossips = [
        {
            "title": "Anitta revela novo relacionamento em entrevista exclusiva",
            "content": "A cantora confirmou romance com empresário durante programa de TV",
            "celebrity": "Anitta",
            "category": "relacionamento",
            "score": 8.5,
            "source": "UOL Splash",
            "url": "https://splash.uol.com.br/fake-news-1"
        },
        {
            "title": "Bruna Marquezine é vista em jantar romântico",
            "content": "Atriz foi fotografada em restaurante exclusivo de São Paulo",
            "celebrity": "Bruna Marquezine", 
            "category": "relacionamento",
            "score": 7.8,
            "source": "CARAS",
            "url": "https://caras.uol.com.br/fake-news-2"
        },
        {
            "title": "Xuxa anuncia novo projeto na televisão",
            "content": "Apresentadora retorna com programa infantil em nova emissora",
            "celebrity": "Xuxa",
            "category": "carreira",
            "score": 7.2,
            "source": "F5",
            "url": "https://f5.folha.uol.com.br/fake-news-3"
        }
    ]
    
    # Filtrar por score mínimo
    filtered_gossips = [g for g in fake_gossips if g['score'] >= min_score]
    
    # Limitar quantidade
    result_gossips = filtered_gossips[:limit]
    
    return jsonify({
        "success": True,
        "data": {
            "gossips": result_gossips,
            "total_found": len(result_gossips),
            "categories": list(set([g['category'] for g in result_gossips])),
            "search_params": {
                "limit": limit,
                "min_score": min_score
            }
        }
    })

@app.route('/n8n/script/generate', methods=['POST'])
def generate_script():
    """Gerar roteiro para n8n"""
    data = request.get_json() or {}
    gossips = data.get('gossips', [])
    target_duration = data.get('target_duration', 6)
    
    # Simular geração de roteiro
    script_data = {
        "episode_info": {
            "theme": f"Fofocas do Dia - {len(gossips)} Histórias Quentes",
            "duration_minutes": target_duration,
            "segments": len(gossips) + 2,  # +2 para intro e outro
            "date": "01/07/2025"
        },
        "script": {
            "intro": "Olá pessoal! Bem-vindos ao nosso podcast de fofocas! Eu sou a Jennifer e comigo está o David. Hoje temos histórias incríveis para vocês!",
            "segments": [
                {
                    "speaker": "Jennifer",
                    "content": f"Vamos começar falando sobre {gossips[0]['celebrity'] if gossips else 'as celebridades'}...",
                    "duration": 90
                },
                {
                    "speaker": "David", 
                    "content": "Que história interessante! E vocês sabiam que...",
                    "duration": 120
                }
            ],
            "outro": "E por hoje é só pessoal! Não esqueçam de se inscrever e ativar o sininho!"
        },
        "audio_segments": [
            {
                "speaker": "Jennifer",
                "text": "Olá pessoal! Bem-vindos ao nosso podcast de fofocas!",
                "voice_type": "female_voice"
            },
            {
                "speaker": "David",
                "text": "Oi gente! Hoje temos histórias incríveis!",
                "voice_type": "male_voice"
            }
        ]
    }
    
    return jsonify({
        "success": True,
        "data": script_data
    })

@app.route('/n8n/cover/generate', methods=['POST'])
def generate_cover():
    """Gerar capa para n8n"""
    data = request.get_json() or {}
    episode_data = data.get('episode_data', {})
    
    # Simular geração de capa
    cover_data = {
        "cover_info": {
            "theme": episode_data.get('episode_theme', 'Fofocas do Dia'),
            "style": "modern_podcast",
            "colors": ["#FF6B9D", "#4ECDC4", "#45B7D1"],
            "elements": ["microphone", "sparkles", "celebrity_silhouette"]
        },
        "file_info": {
            "filename": "podcast_cover_20250701.png",
            "format": "PNG",
            "dimensions": "1400x1400",
            "size_mb": 2.1
        },
        "download_url": "http://localhost:5000/download/image/podcast_cover_20250701.png"
    }
    
    return jsonify({
        "success": True,
        "data": cover_data
    })

@app.route('/n8n/audio/generate', methods=['POST'])
def generate_audio():
    """Gerar áudio para n8n"""
    data = request.get_json() or {}
    audio_segments = data.get('audio_segments', [])
    
    # Simular geração de áudio
    audio_data = {
        "audio_info": {
            "duration_seconds": 360,
            "format": "MP3",
            "quality": "high",
            "sample_rate": "44.1kHz",
            "segments_processed": len(audio_segments)
        },
        "file_info": {
            "filename": "podcast_episode_20250701.mp3",
            "size_mb": 8.5
        },
        "download_url": "http://localhost:5000/download/audio/podcast_episode_20250701.mp3"
    }
    
    return jsonify({
        "success": True,
        "data": audio_data
    })

@app.route('/n8n/video/generate', methods=['POST'])
def generate_video():
    """Gerar vídeo para n8n"""
    data = request.get_json() or {}
    video_type = data.get('type', 'reel')
    episode_data = data.get('episode_data', {})
    
    # Simular geração de vídeo
    video_data = {
        "video_info": {
            "type": video_type,
            "duration_seconds": 30 if video_type == 'reel' else 60,
            "format": "MP4",
            "resolution": "1080x1920" if video_type == 'reel' else "1920x1080",
            "fps": 30
        },
        "file_info": {
            "filename": f"podcast_{video_type}_20250701.mp4",
            "size_mb": 15.2
        },
        "download_url": f"http://localhost:5000/download/video/podcast_{video_type}_20250701.mp4"
    }
    
    return jsonify({
        "success": True,
        "data": video_data
    })

if __name__ == '__main__':
    print("🎙️ Iniciando API de teste para n8n...")
    print("📡 Endpoints disponíveis:")
    print("   GET  /n8n/health")
    print("   GET  /n8n/status") 
    print("   POST /n8n/gossips/search")
    print("   POST /n8n/script/generate")
    print("   POST /n8n/cover/generate")
    print("   POST /n8n/audio/generate")
    print("   POST /n8n/video/generate")
    print("🚀 API rodando em http://localhost:5000")
    
    app.run(host='0.0.0.0', port=5000, debug=True)

