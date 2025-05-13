/**
 * Converts a hash to a string with a given encoding.
 * @example
 * ```ts
 * import { crypto } from "https://deno.land/std@$STD_VERSION/crypto/crypto.ts";
 * import { toHashString } from "https://deno.land/std@$STD_VERSION/crypto/to_hash_string.ts"
 *
 * const hash = await crypto.subtle.digest("SHA-384", new TextEncoder().encode("You hear that Mr. Anderson?"));
 *
 * // Hex encoding by default
 * console.log(toHashString(hash));
 *
 * // Or with base64 encoding
 * console.log(toHashString(hash, "base64"));
 * ```
 */
export declare function toHashString(hash: ArrayBuffer, encoding?: "hex" | "base64"): string;
