from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from prompt import sa
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("api_key")


s = """{"sender_known_malicios":1,
        "sender_domain_reputation_score":0.02,
        "sender_spoof_detected":1,
        "sender_temp_email_likelihood":0.95,
        "dmarc_enforced":0,
        "packer_detected":1,
        "any_file_hash_malicious":1,
        "max_metadata_suspicious_score":0.89,
        "malicious_attachment_Count":2,
        "has_executable_attachment":1,
        "unscannable_attachment_present":0,
        "total_yara_match_count":15,
        "total_ioc_count":23,
        "max_behavioral_sandbox_score":0.94,
        "max_amsi_suspicion_score":0.88,
        "any_macro_enabled_document":1,
        "any_vbscript_javascript_detected":1,
        "any_active_x_objects_detected":0,
        "any_network_call_on_open":1,
        "max_exfiltration_behavior_score":0.91,
        "any_exploit_pattern_detected":1,
        "total_embedded_file_count":3,
        "max_suspicious_string_entropy_score":0.92,
        "max_sandbox_execution_time":45.7,
        "unique_parent_process_names":"[\"cmd.exe\", \"powershell.exe\"]",
        "return_path_mismatch_with_from":1,
        "return_path_known_malicious":1,
        "return_path_reputation_score":0.03,
        "reply_path_known_malicious":1,
        "reply_path_diff_from_sender":1,
        "reply_path_reputation_Score":0.01,
        "smtp_ip_known_malicious":1,
        "smtp_ip_geo":0.98,
        "smtp_ip_asn":0.95,
        "smtp_ip_reputation_score":0.01,
        "domain_known_malicious":1,
        "url_Count":3,
        "dna_morphing_detected":1,
        "domain_tech_stack_match_score":0.95,
        "is_high_risk_role_targeted":1,
        "sender_name_similarity_to_vip":0.87,
        "urgency_keywords_present":1,
        "request_type":"wire_transfer",
        "content_spam_score":0.15,
        "user_marked_as_spam_before":0,
        "bulk_message_indicator":0,
        "unsubscribe_link_present":0,
        "marketing-keywords_detected":0.0,
        "html_text_ratio":0.1,
        "image_only_email":0,
        "spf_result":"fail",
        "dkim_result":"fail",
        "dmarc_result":"fail",
        "reverse_dns_valid":0,
        "tls_version":"TLS 1.0",
        "total_links_detected":3,
        "url_shortener_detected":1,
        "url_redirect_chain_length":4,
        "final_url_known_malicious":1,
        "url_decoded_spoof_detected":1,
        "url_reputation_score":0.02,
        "ssl_validity_status":"expired",
        "site_visual_similarity_to_known_brand":0.94,
        "url_rendering_behavior_score":0.89,
        "link_rewritten_through_redirector":0,
        "token_validation_success":0,
        "total_components_detected_malicious":5,}"""
label = "Mlicious"
em = "We've noticed unusual activity on your account. Please click here immediately to verify your identity: http://amaz0n-verify.com/secure/login\n\nFailure to verify within 24 hours will result in account suspension.\n\nAmazon Security Team"

# inp = f"this is my 68 signals {s} extract from email. This my email content {em}. This classification output {label}"


def summary_genrator(inp):
    # Initialize LLM with API ke
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", temperature=0, api_key=API_KEY
    )

    messages = [SystemMessage(content=sa), HumanMessage(content=inp)]
    response = llm.invoke(messages)
    # print(response.content)
    return response.content
